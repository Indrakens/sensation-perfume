from django.shortcuts import (
    render, reverse, redirect, get_object_or_404, HttpResponseRedirect)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Review, Category, Brand, Genders
from .forms import ProductForm


def all_products(request):
    """A view to show all products"""

    products = Product.objects.all()
    brand_list = Brand.objects.all()
    gender_list = Genders.objects.all()
    query = None
    categories = None
    brands = None
    genders = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "brand" in request.GET:
            brands = request.GET["brand"].split(",")
            products = products.filter(brand__name__in=brands)
            brands = Category.objects.filter(name__in=brands)

        if "gender" in request.GET:
            genders = request.Get["gender"].split(',')
            products = products.filter(genders__name__in=genders)
            gender = Genders.objects.filter(name__in=genders)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(product_description__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show each product details"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
                messages.success(request, "Successfully added review!")
            else:
                review = Review.objects.create(
                product=product,
                rating=rating,
                content=content,
                created_by=request.user
                )

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can access.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please check the form."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    """Update a product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can access.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please check the form."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/update_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can access.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Product {product.name} deleted!")
    return redirect(reverse("products"))    

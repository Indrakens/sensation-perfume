# Generated by Django 3.2.23 on 2024-02-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20240202_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_full_name',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='order',
            name='user_surname',
            field=models.CharField(default='surname', max_length=50),
        ),
    ]
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _ 


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('') 
    template_name = 'profiles/custom_widget_template/custom_clearable_file.html' 

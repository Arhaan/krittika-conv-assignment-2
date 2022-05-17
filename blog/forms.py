from django import forms
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Post, CATEGORIES
class PostCreateForm(forms.Form):
    title = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES)
    content = forms.CharField(widget=CKEditorWidget(), required=True)
   

    class Meta:
        model = Post
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'posts-create'

        self.helper.add_input(Submit('submit', 'Submit'))
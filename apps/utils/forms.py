from django import forms
from ckeditor.widgets import CKEditorWidget

from .base_form import FormsMixin


class CommentForm(forms.Form, FormsMixin):
    content =forms.CharField()


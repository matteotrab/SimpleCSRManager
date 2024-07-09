from django import forms
from .models import Requirement, Document

class RequirementForm(forms.ModelForm):
    documents = forms.ModelMultipleChoiceField(
        queryset=Document.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Requirement
        fields = ['title', 'description', 'documents']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'isValidated']

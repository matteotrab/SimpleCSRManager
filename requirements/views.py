from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Requirement, Document
from .forms import RequirementForm, DocumentForm

def toggle_validation_status(request, doc_id):
    document = get_object_or_404(Document, pk=doc_id)
    document.isValidated = not document.isValidated
    document.save()
    req_id = request.GET.get('req_id', False)
    for requirement in document.requirements.all():
        requirement.updateComplianceStatus()
        requirement.save()
    # Redirect back to the requirement detail view that contains this document
    if req_id is not False:
        return redirect('requirement_detail', pk=req_id)
    return redirect('document_list')

def requirement_list(request):
    requirements = Requirement.objects.all()
    return render(request, 'requirements/requirement_list.html', {'requirements': requirements})

def requirement_detail(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    documents = requirement.documents.all()
    return render(request, 'requirements/requirement_detail.html', {'requirement': requirement, 'documents': documents})

def requirement_new(request):
    if request.method == "POST":
        form = RequirementForm(request.POST)
        if form.is_valid():
            requirement = form.save()
            requirement.updateComplianceStatus()
            requirement.save()
            return redirect('requirement_detail', pk=requirement.pk)
    else:
        form = RequirementForm()
    return render(request, 'requirements/requirement_edit.html', {'form': form})

def requirement_edit(request, pk):
    requirement = get_object_or_404(Requirement, pk=pk)
    if request.method == "POST":
        form = RequirementForm(request.POST, instance=requirement)
        if form.is_valid():
            requirement = form.save()
            requirement.updateComplianceStatus()
            requirement.save()
            return redirect('requirement_detail', pk=requirement.pk)
    else:
        form = RequirementForm(instance=requirement)
    return render(request, 'requirements/requirement_edit.html', {'form': form})

def requirement_delete(request, pk):
    next_url = request.GET.get('next', 'requirement_list')
    requirement = get_object_or_404(Requirement, pk=pk)
    requirement.delete()
    return redirect(next_url)

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'requirements/document_list.html', {'documents': documents})


def document_new(request):
    next_url = request.GET.get('next', 'requirement_list')
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save()
            return redirect(next_url)
    else:
        form = DocumentForm()
    return render(request, 'requirements/document_edit.html', {'form': form, 'next': next_url})

def document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    next_url = request.GET.get('next', 'requirement_list')  # Default to 'requirement_list' if 'next' is not provided
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save()
            for requirement in document.requirements.all():
                requirement.updateComplianceStatus()
                requirement.save()
            return redirect(next_url)
    else:
        form = DocumentForm(instance=document)
    return render(request, 'requirements/document_edit.html', {'form': form, 'next': next_url})

def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    requirements = document.requirements.all()
    return render(request, 'requirements/document_detail.html', {'requirements': requirements, 'document': document})

def document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    next_url = request.GET.get('next', 'requirement_list')
    document.isValidated = True
    document.save()
    for requirement in document.requirements.all():
        requirement.updateComplianceStatus()
        requirement.save()
    document.delete()
    return redirect(next_url)

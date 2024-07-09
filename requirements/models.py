from django.db import models

# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isValidated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Requirement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isCompliant = models.BooleanField(default=False)
    documents = models.ManyToManyField(Document, blank=True, related_name='requirements')
    
    def updateComplianceStatus(self):
        self.isCompliant = True
        for document in self.documents.all():
            if not document.isValidated:
                self.isCompliant = False
    
    def __str__(self):
        return self.title

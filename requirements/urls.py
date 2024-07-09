from django.urls import path
from . import views

urlpatterns = [
    path('', views.requirement_list, name='requirement_list'),
    path('requirement/<int:pk>/', views.requirement_detail, name='requirement_detail'),
    path('requirement/new/', views.requirement_new, name='requirement_new'),
    path('requirement/<int:pk>/edit/', views.requirement_edit, name='requirement_edit'),
    path('requirement/<int:pk>/delete/', views.requirement_delete, name='requirement_delete'),
    path('document/', views.document_list, name='document_list'),
    path('document/new/', views.document_new, name='document_new'),
    path('document/<int:pk>/edit/', views.document_edit, name='document_edit'),
    #path('document/<int:doc_id>/<int:req_id>/toggle_validation/', views.toggle_validation_status, name='toggle_validation_status'),
    path('document/<int:doc_id>/toggle_validation/', views.toggle_validation_status, name='toggle_validation_status'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('document/<int:pk>/delete/', views.document_delete, name='document_delete'),
]

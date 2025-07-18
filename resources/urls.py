from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('actsbills/', views.document_list, {'category_name': 'Acts'}, name='acts'),
    path('reports/', views.document_list, {'category_name': 'Reports'}, name='reports'),
    path('careers/', views.document_list, {'category_name': 'Careers'}, name='careers'),
    path('kdsp/', views.document_list, {'category_name': 'KDSP'}, name='kdsp'),
    path('bursaries/', views.document_list, {'category_name': 'Bursaries'}, name='bursaries'),
    path('other-downloads/', views.document_list, {'category_name': 'Other Downloads'}, name='other_downloads'),
    path('budgets/', views.document_list, {'category_name': 'Budget'}, name='budget'),
    path('tenders/', views.document_list, {'category_name': 'Tenders'}, name='tenders'),
]
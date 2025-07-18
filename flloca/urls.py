from django.urls import path
from . import views

app_name = 'flloca'

urlpatterns = [
    path('', views.flloca_index, name='flloca_index'),
    path('projects',views.project_list, name='project_list'),
    path('about',views.about, name='about'),
    path('grievance/',views.grievance, name='grievance'),
    path('projects/<slug:slug>', views.project_detail, name='project_detail'),
    path('other-downloads/', views.flloca_view, {'category_name': 'Other Downloads'}, name='other_downloads'),
    path('loadging/', views.flloca_view, {'category_name': 'Loadging'}, name='loadging'),
    #path('grievance/', views.flloca_view, {'category_name': 'Grievance'}, name='grievance'),
    path('grievance-report/', views.flloca_view, {'category_name': 'Grievance Report'}, name='grievance_report'),
    path('loadging/', views.flloca_view, {'category_name': 'Loadging'}, name='loadging'),
    path('strategic-plan/', views.flloca_view, {'category_name': 'Strategic Plan'}, name='strategic_plan'),
  
]
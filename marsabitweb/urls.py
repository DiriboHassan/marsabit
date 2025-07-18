from django.urls import path

from . import views 

from django.conf import settings
from django.conf.urls.static import static
from .views import DetailView



app_name = 'marsabitweb'

urlpatterns =[
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('gallery',views.gallery, name='gallery'),
    path('news',views.news_list, name='news_list'),
    path('news/<slug:name>', views.news_detail, name='news_detail'),
    path('projects',views.project_list, name='project_list'),
    path('projects/<slug:name>', views.project_detail, name='project_detail'),
    path('departments',views.departments_list, name='departments_list'),
    path('departments/<slug:name>', views.departments_detail, name='departments_detail'),
    path('executives/<slug:name>', views.executives, name='executives'),
    path('co',views.chiefofficer_list, name='chiefofficer_list'),
    path('co/<slug:title>', views.chiefofficer_detail, name='chiefofficer_detail'),
    path('cecm',views.cecm_list, name='cecm_list'),
    path('cecm/<slug:title>', views.cecm_detail, name='cecm_detail'),
    path('governor', views.governor_detail, name='governor_detail'),
    path('depgov', views.depgov_detail, name='depgov_detail'),
    path('speaker', views.speaker_detail, name='speaker_detail'),
    path('cs', views.cs_detail, name='cs_detail'),
    #path('specific/<slug:slug>', views.specific_executives, name='specific_executives'),
   
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
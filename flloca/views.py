from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Document, Category, DeptHeads, OurProjects, Introduction, Services, FllocaGallery, HeroFlloca, GrievanceSteps
from marsabitweb.models import Copyright, HeroOthers, Executives
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
# Create your views here.


def flloca_index(request):
    intros = Introduction.objects.all()
    heroflloca = HeroFlloca.objects.all()
    gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:4]
    services = Services.objects.all()[:4]              
    projects = OurProjects.objects.all().order_by('-created_date')[:3]
    copyrights = Copyright.objects.all()
    specific_titles = ['CEC', 'CO1', 'CO2', 'CO3']
    executives = DeptHeads.objects.filter(title__in=specific_titles)[:4]
    print(f"Specific executives: {[executives.title for executives in executives]}")
    

    return render (request, 'flloca/flloca.html', { 'intros': intros, 'heroflloca': heroflloca, 'gallery':gallery, 'services': services, 'projects':projects, 'copyrights': copyrights, 'executives': executives})
 

def about(request):
     intros = Introduction.objects.all()
     grievances = GrievanceSteps.objects.all()
     heroflloca = HeroFlloca.objects.all()
     gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['About']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     copyrights = Copyright.objects.all()
     specific_titles = ['CEC', 'CO1', 'CO2', 'CO3']
     executives = DeptHeads.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     return render (request, 'flloca/about.html', {'grievances': grievances, 'intros': intros, 'hero_others': hero_others, 'heroflloca': heroflloca, 'gallery':gallery, 'copyrights':copyrights, 'executives': executives})




def grievance(request):
     grievances = GrievanceSteps.objects.all()
     intros = Introduction.objects.all()
     heroflloca = HeroFlloca.objects.all()
     gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['About']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     copyrights = Copyright.objects.all()
     specific_titles = ['CEC', 'CO1', 'CO2', 'CO3']
     executives = DeptHeads.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     return render (request, 'flloca/grievance.html', {'grievances': grievances, 'intros': intros, 'hero_others': hero_others, 'heroflloca': heroflloca, 'gallery':gallery, 'copyrights':copyrights, 'executives': executives})



def flloca_view(request, category_name):
    intros = Introduction.objects.all()
    grievances = GrievanceSteps.objects.all()
    heroflloca = HeroFlloca.objects.all()
    gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:6]
    specific_titles = ['About']
    copyrights = Copyright.objects.all()

    category = Category.objects.get(name=category_name)
    documents = Document.objects.filter(category=category)
    return render(request, f'flloca/{category_name.lower()}.html', {
        'documents': documents,
        'category_name': category_name,
        'intros': intros, 
        'heroflloca': heroflloca, 'gallery':gallery, 
        'copyrights':copyrights,
        'specific_titles':specific_titles,
        'grievances' : grievances,

    })



def project_list(request):
     intros = Introduction.objects.all()
     grievances = GrievanceSteps.objects.all()
     heroflloca = HeroFlloca.objects.all()
     gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['Projects']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     project_list = OurProjects.objects.all().order_by('-created_date')
     copyrights = Copyright.objects.all()
     specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")

     return render (request, 'flloca/projects.html', {'specific_titles':specific_titles, 'executives':executives,'grievances':grievances, 'intros': intros, 'heroflloca': heroflloca,'gallery':gallery, 'hero_others': hero_others, 'project_list': project_list, 'copyrights':copyrights})

# single news itemview

def project_detail(request, slug):
     intros = Introduction.objects.all()
     grievances = GrievanceSteps.objects.all()
     heroflloca = HeroFlloca.objects.all()
     gallery = FllocaGallery.objects.all().order_by('-uploaded_at')[:6]
     project_item = get_object_or_404(OurProjects, slug=slug)
     copyrights = Copyright.objects.all()
     specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")

    
     return render (request, 'flloca/projects_single.html', {'specific_titles':specific_titles, 'executives':executives, 'grievances':grievances, 'intros': intros, 'heroflloca': heroflloca,'gallery':gallery, 'project_item': project_item, 'copyrights':copyrights})
    
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Introduction
from .models import Hero
from .models import Services
from .models import News
from .models import Projects
from .models import Departments
from .models import Executives
from .models import Deptheads
from .models import HeroOthers
from .models import Copyright
from .models import Gallery
from .models import About
from .models import PromotionalVideo
from contact.models import ContactSubmission
from contact.forms import ContactForm
from .models import Partners

from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    intros = Introduction.objects.all()
    heros = Hero.objects.all()
    partners = Partners.objects.all().order_by('-posted_on')[:4]
    gallery = Gallery.objects.all().order_by('-uploaded_at')[:4]
    services = Services.objects.all()[:4]              
    news = News.objects.all().order_by('-created_date')[:3]
    projects = Projects.objects.all().order_by('-created_date')[:3]
    promotional_video = PromotionalVideo.objects.filter(is_active=True).first()
    copyrights = Copyright.objects.all()
    form = ContactForm(request.POST)
    departments_list = Departments.objects.all().order_by('-created_date')[:3]
    specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
    executives = Executives.objects.filter(title__in=specific_titles)[:4]
    print(f"Specific executives: {[executives.title for executives in executives]}")
    

    return render (request, 'index.html', {'form':form, 'intros': intros, 'partners':partners, 'heros': heros, 'gallery':gallery, 'services': services, 'news':news,  'projects':projects, 'promotional_video':promotional_video, 'copyrights': copyrights, 'departments_list':departments_list, 'executives': executives})
 


def about(request):
     about = About.objects.all()
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['About']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     copyrights = Copyright.objects.all()
     specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     return render (request, 'about.html', {'about':about, 'intros': intros, 'hero_others': hero_others, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'executives': executives})

def gallery(request):
     gallery = Gallery.objects.all()
     intros = Introduction.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     heros = Hero.objects.all()
     specific_titles = ['Gallery']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     copyrights = Copyright.objects.all()
     specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     return render (request, 'gallery.html', {'gallery': gallery, 'intros': intros, 'hero_others': hero_others,'gallery':gallery, 'heros': heros, 'copyrights':copyrights, 'executives': executives})


def contact(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['Contact']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     copyrights = Copyright.objects.all()
     return render (request, 'contact.html', {'intros': intros, 'hero_others': hero_others, 'heros': heros,'gallery':gallery, 'copyrights':copyrights})




def news_list(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['News']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     news_list = News.objects.all().order_by('-created_date')
     copyrights = Copyright.objects.all()
     

     return render (request, 'news.html', {'intros': intros, 'heros': heros, 'hero_others': hero_others,'gallery':gallery, 'news_list':news_list, 'copyrights':copyrights})

# single news item view

def news_detail(request, name):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['News']
     specific_title = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_title)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     news_item = get_object_or_404(News, name=name)
     copyrights = Copyright.objects.all()

    
     return render (request, 'news_single.html', {'intros': intros, 'heros': heros,'gallery':gallery, 'news_item': news_item, 'executives': executives, 'copyrights':copyrights})
    

def project_list(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['Projects']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     project_list = Projects.objects.all().order_by('-created_date')
     copyrights = Copyright.objects.all()
     specific_title = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_title)[:4]

     return render (request, 'projects.html', {'specific_title':specific_title, 'executives':executives, 'intros': intros, 'heros': heros,'gallery':gallery, 'hero_others': hero_others, 'project_list': project_list, 'copyrights':copyrights})

# single news itemview

def project_detail(request, name):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     project_item = get_object_or_404(Projects, name=name)
     copyrights = Copyright.objects.all()
     specific_title = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_title)[:4]

    
     return render (request, 'projects_single.html', {'specific_title':specific_title, 'executives':executives, 'intros': intros, 'heros': heros,'gallery':gallery, 'project_item': project_item, 'copyrights':copyrights})
    

def departments_list(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['Departments']
     hero_others = HeroOthers.objects.filter(title__in=specific_titles)
     departments_list = Departments.objects.all().order_by('-created_date')
     copyrights = Copyright.objects.all()
     

     return render (request, 'departments.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'hero_others': hero_others, 'departments_list': departments_list, 'copyrights':copyrights})

# single news item view

def departments_detail(request, name):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     #hero_others = HeroOthers.objects.all()
     specific_title = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_title)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")
     departments_item = get_object_or_404(Departments, name=name)
     copyrights = Copyright.objects.all()

    
     return render (request, 'departments_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'departments_item': departments_item, 'executives': executives, 'copyrights':copyrights})


def executives(request):
     
     specific_titles = ['Marsabit County Governor', 'Deputy Governor', 'Speaker Of The County Assembly', 'County Secretary']
     executives = Executives.objects.filter(title__in=specific_titles)[:4]
     print(f"Specific executives: {[executives.title for executives in executives]}")


     return render(request, 'index.html', {'executives': executives})


def cecm_list(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['CECM']
     cecm_list = Deptheads.objects.filter(title__in=specific_titles)
     

     return render (request, 'cecm.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'cecm_list':cecm_list})



def cecm_detail(request, title):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['CECM']
     cecm_item = get_object_or_404(Deptheads.objects.filter(title__in=specific_titles), title=title)
     copyrights = Copyright.objects.all()

    
     return render (request, 'cecm_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'cecm_item': cecm_item, 'copyrights':copyrights})

def chiefofficer_list(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['CO']
     chiefofficer_list = Deptheads.objects.filter(title__in=specific_titles)
     

     return render (request, 'chiefofficers.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'chiefofficer_list':chiefofficer_list})



def chiefofficer_detail(request, title):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     specific_titles = ['CO']
     chiefofficer_item = get_object_or_404(Deptheads.objects.filter(title__in=specific_titles), title=title)
     copyrights = Copyright.objects.all()

    
     return render (request, 'chiefofficer_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'chiefofficer_item': chiefofficer_item, 'copyrights':copyrights})



def governor_detail(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['Marsabit County Governor']
     governor_item = Executives.objects.get(title__in=specific_titles)

    
     return render (request, 'governor_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'governor_item': governor_item})



def depgov_detail(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['Deputy Governor']
     depgov_item = Executives.objects.get(title__in=specific_titles)

    
     return render (request, 'depgov_single.html', {'intros': intros, 'heros': heros,'gallery':gallery,  'copyrights':copyrights, 'depgov_item': depgov_item})


def speaker_detail(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['Speaker Of The County Assembly']
     speaker_item = Executives.objects.get(title__in=specific_titles)
    
     return render (request, 'speaker_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'speaker_item': speaker_item})


def cs_detail(request):
     intros = Introduction.objects.all()
     heros = Hero.objects.all()
     gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
     copyrights = Copyright.objects.all()
     specific_titles = ['County Secretary']
     cs_item = Executives.objects.get(title__in=specific_titles)

    
     return render (request, 'cs_single.html', {'intros': intros, 'heros': heros, 'gallery':gallery, 'copyrights':copyrights, 'cs_item': cs_item})

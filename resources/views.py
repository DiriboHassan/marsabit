from django.shortcuts import render
from .models import Document, Category
from marsabitweb.models import Hero, Introduction, Gallery, Copyright

def document_list(request, category_name):
    intros = Introduction.objects.all()
    heros = Hero.objects.all()
    gallery = Gallery.objects.all().order_by('-uploaded_at')[:6]
    specific_titles = ['About']
    copyrights = Copyright.objects.all()

    category = Category.objects.get(name=category_name)
    documents = Document.objects.filter(category=category)
    return render(request, f'resources/{category_name.lower()}.html', {
        'documents': documents,
        'category_name': category_name,
        'intros': intros, 
        'heros': heros, 'gallery':gallery, 
        'copyrights':copyrights,
        'specific_titles':specific_titles,

    })
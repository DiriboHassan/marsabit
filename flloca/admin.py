from django.contrib import admin
from .models import Category, Document, Introduction, FllocaGallery, Services, HeroFlloca, OurProjects, DeptHeads, GrievanceSteps

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')

admin.site.register(Introduction)
admin.site.register(FllocaGallery)
admin.site.register(Services)
admin.site.register(HeroFlloca)
admin.site.register(OurProjects)
admin.site.register(DeptHeads)
admin.site.register(GrievanceSteps)

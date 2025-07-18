from django.contrib import admin
from .models import Introduction, Hero, Services, News, Projects, Departments, HeroOthers, Executives, Deptheads,Copyright, Gallery, PromotionalVideo, Partners, About

# Register your models here.

admin.site.register(Introduction)
admin.site.register(Hero)
admin.site.register(Services)
admin.site.register(News)
admin.site.register(Projects)
admin.site.register(Departments)
admin.site.register(Executives)
admin.site.register(Deptheads)
admin.site.register(HeroOthers)
admin.site.register(Copyright)
admin.site.register(Gallery)
admin.site.register(Partners)
admin.site.register(About)
@admin.register(PromotionalVideo)

class PromotionalVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'uploaded_at')
    list_filter = ('is_active', 'uploaded_at')
    search_fields = ('title',)
    def save_model(self, request, obj, form, change):
        if obj.is_active:
            PromotionalVideo.objects.filter(is_active=True).exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)



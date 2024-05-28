from django.contrib import admin
from .models import (Biz_haqimizda,
                     Comment,
                     User,
                     Profile,
                     Team,
                     Social_media,
                     Book,
                     Category)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name', 'id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Biz_haqimizda)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Social_media)
admin.site.register(Book)
admin.site.register(Team)

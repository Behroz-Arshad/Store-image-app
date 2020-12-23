from django.contrib import admin
from RanaFurniture.models import Category, Image, Promotion


# Register your models here.

class CategoryAdmin( admin.ModelAdmin ):
    fieldsets = [(None, {'fields': ['title']}), (None, {'fields': ['description']})]
    list_display = ('title', 'description')
    search_fields = ['title']


admin.site.register( Category, CategoryAdmin )


class ImageAdmin( admin.ModelAdmin ):
    fieldsets = [(None, {'fields': ['title']}), (None, {'fields': ['description']}), (None, {'fields': ['image']}),
                 (None, {'fields': ['category']})]
    list_display = ('title', 'description', 'image', 'added_date', 'category')
    search_fields = ['title']


admin.site.register( Image, ImageAdmin )


class PromotionAdmin( admin.ModelAdmin ):
    fieldsets = [(None, {'fields': ['promotion_image']}), (None, {'fields': ['is_active']})]
    list_display = ('promotion_image', 'is_active')


admin.site.register( Promotion, PromotionAdmin )

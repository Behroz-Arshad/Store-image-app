from django.urls import path
from RanaFurniture.views import Index, CategoryById, Contact
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<int:pk>', CategoryById.as_view(), name='categoryByID'),
    path('contact', Contact.as_view(), name='contact')
]
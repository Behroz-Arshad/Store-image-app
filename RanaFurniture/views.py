from django.shortcuts import render
from RanaFurniture.models import Image, Category
from django.views import generic


# Create your views here.

class Index(generic.ListView):
    context_object_name = 'images'
    template_name = 'RanaFurniture/index.html'

    def get_queryset(self):
        return Image.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        return context


class CategoryById(generic.View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        query = Category.objects.get(pk=self.kwargs['pk'])
        images = Image.objects.filter(category=query)
        data = {'images': images, 'categories': categories}

        return render(request, 'RanaFurniture/index.html', data)


class Contact(generic.TemplateView):
    template_name = 'RanaFurniture/contact.html'
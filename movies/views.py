from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView, MultipleObjectMixin
from movies.models import Categories, Villans
from django.views.generic import TemplateView
from movies.forms import Search
from django.db.models import Q



class SearchForm(object):
    def get_context_data(self, **kwargs):
        context = super(SearchForm, self).get_context_data(**kwargs)
        context['form_search'] = Search()
        return context


class Home(SearchForm,TemplateView):
    template_name = "index.html"



class AddCategory(SearchForm,CreateView):
    model = Categories
    fields = ['category']
    template_name = "forms.html"
    context_object_name = "context"





class ListVillans(SearchForm,ListView):
    template_name = "index.html"
    context_object_name = "content"
    queryset = Villans.objects.all()
    paginate_by = 2




class AddVillans(SearchForm,CreateView):
    model = Villans
    fields = '__all__'
    template_name = "forms.html"



class UpdateVillans(UpdateView):
    model = Villans
    fields = '__all__'
    template_name = "forms.html"


class Searchview(SearchForm,ListView):
    template_name = "index.html"
    context_object_name = "content"
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')
        category = self.request.GET.get('categories',0)
        context = Villans.objects.filter(name__icontains=search)
        if int(category):
            context = context.filter(category__id=category)
        return context


class villanDetail(SearchForm,DetailView):
    template_name = "index.html"
    model = Villans
    context_object_name = "details"

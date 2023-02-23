from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Tech,Book


class PortListView(ListView):
    model = Tech
    template_name = 'xtech/index.html'
    context_object_name = 'techs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class UploadPortView(CreateView):
    model = Tech
    fields = ('title', 'pdf', 'cover')
    success_url = reverse_lazy('xtech:index')
    template_name = 'xtech/upload.html'

class BookListView(ListView):
    model = Book
    template_name = 'xtech/index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['techs'] = Tech.objects.all()
        return context

class UploadBookView(CreateView):
    model = Book
    fields = ('site_name','site_url','site_con','site_cover')
    success_url = reverse_lazy('xtech:index')
    template_name = 'xtech/create.html'


def delete(req,pk):
    if req.method == 'POST':
        tech = Tech.objects.get(pk=pk)
        tech.delete()
        return redirect('xtech:index')

def delete_book(req,pk):
    if req.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('xtech:index')
# Create your views here.
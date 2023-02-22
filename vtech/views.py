from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Tech


class PortListView(ListView):
    model = Tech
    template_name = 'vtech/index.html'
    context_object_name = 'techs'

class UploadPortView(CreateView):
    model = Tech
    fields = ('title', 'pdf', 'cover')
    success_url = reverse_lazy('vtech:index')
    template_name = 'vtech/upload.html'

def delete(req,pk):
    if req.method == 'POST':
        tech = Tech.objects.get(pk=pk)
        tech.delete()
        return redirect('vtech:index')

# Create your views here.

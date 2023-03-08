from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GuestForm
from .models import Guest

def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.writer = request.user
            guest.save()
            return redirect('guestbook:index')
    else:
        form = GuestForm()
    
    guests = Guest.objects.order_by('-created_at')
    return render(request, 'guestbook/index.html', {'form': form, 'guests':guests})

def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, id=guest_id)
    guest.delete()
    return redirect('guestbook:index')
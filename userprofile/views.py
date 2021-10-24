from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm


# Create your views here.
@login_required
def userprofile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm()
    return render(
        request, "userprofile/profile.html", {'form': form}
    )

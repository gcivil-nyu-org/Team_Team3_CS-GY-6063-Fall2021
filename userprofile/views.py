from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserDeleteProfileForm, UserUpdateForm, ProfileUpdateForm


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            msg = "Your account has been updated!"
            messages.success(request, f"{msg}")
            return redirect("home")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "userprofile/edit_profile.html", context)

@login_required
def profile_page(request):

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "userprofile/profile_page.html", context)

@login_required
def delete_profile(request):
    if request.method == "POST":
        delete_form = UserDeleteProfileForm(request.POST, instance=request.user)

        if delete_form.is_valid():

            try:
                u = User.objects.get(username = request.user)
                u.delete()
                messages.success(request, "The user is deleted")            

            except User.DoesNotExist:
                messages.error(request, "User does not exist")

            # user = request.user
            # user.delete()

            # user_pk = request.user.pk
            # auth_logout(request)
            # User = get_user_model()
            # User.objects.filter(pk=user_pk).delete()

            messages.info(request, 'Your account has been deleted.')
            return redirect('home')
    else:
        delete_form = UserDeleteProfileForm(instance=request.user)

    context = {
        'delete_form': delete_form
    }

    return render(request, 'userprofile/delete_profile.html', context)

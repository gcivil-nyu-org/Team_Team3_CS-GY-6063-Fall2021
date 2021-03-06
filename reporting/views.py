from django.shortcuts import render
from reporting.forms import ReportNoShowForm,ReportMisbehaviorForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def ContactUs(request):
  return render(request,"reporting/contactus.html")

@login_required
def no_show(request):
  if request.method == "POST":
    f = ReportNoShowForm(request.POST)
    if f.is_valid():
      post = f.save(commit=False)
      post.owner=request.user
      post.save()
      return HttpResponseRedirect(reverse("home"))
  else:
    form = ReportNoShowForm(user=request.user)
    context = {"form": form}
    return render(request, "reporting/noshow.html", context)

@login_required
def misbehavior(request):
  if request.method == "POST":
    f = ReportMisbehaviorForm(request.POST)
    if f.is_valid():
      post = f.save(commit=False)
      post.user=request.user
      post.save()
      return HttpResponseRedirect(reverse("home"))
  else:
    form = ReportMisbehaviorForm(user=request.user)
    context = {"form": form}
    return render(request, "reporting/misbehavior.html", context)

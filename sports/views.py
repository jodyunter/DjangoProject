import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from sports.forms import TeamForm
from sports.models import Team


# Create your views here.
class TeamListView(ListView):
    model = Team
    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        return context

def create(request):
    form = TeamForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("/team/")
        else:            
            return redirect("team/create.html", {"form": form})
                    
    else:
        return render(request, "team/create.html", {"form": form})


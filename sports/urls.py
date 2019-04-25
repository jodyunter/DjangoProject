from django.urls import path
from sports import views
from sports.models import Team

app_name='team'

team_list_view = views.TeamListView.as_view(
    queryset=Team.objects.order_by("-name"),    
    context_object_name="team_list",
    template_name="team/list.html",
)

urlpatterns = [                
    path("create/", views.create, name="create"),
    path("", team_list_view, name="team_list"),
]
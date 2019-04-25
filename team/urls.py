from django.urls import path
from team import views

app_name='team'

urlpatterns = [            
    path("list/", views.teams, name="list"),    
]
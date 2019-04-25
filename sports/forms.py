from django import forms
from sports.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "skill",)
        
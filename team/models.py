from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25)
    skill = models.IntegerField()

    def __str__(self):
        return f"{self.name} Skill:{self.skill}"
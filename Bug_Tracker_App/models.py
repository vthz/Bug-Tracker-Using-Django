from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_desc = models.CharField(max_length=200)
    project_team = models.CharField(max_length=20)

    class Meta:
        db_table = 'Project_Table'


class Bug_table(models.Model):
    project_id = models.CharField(max_length=20)
    bug_desc = models.CharField(max_length=200)
    bug_status = models.CharField(max_length=30)

    class Meta:
        db_table = 'Bug_Table'

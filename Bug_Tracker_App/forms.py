from django import forms
from Bug_Tracker_App.models import Project, Bug_table


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class Bug_tableForm(forms.ModelForm):
    class Meta:
        model = Bug_table
        fields = "__all__"

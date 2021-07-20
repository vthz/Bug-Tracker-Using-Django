from Bug_Tracker_App.forms import ProjectForm, Bug_tableForm
from Bug_Tracker_App.models import Project
from Bug_Tracker_App.models import Bug_table
from django.shortcuts import render, redirect
from django.http import HttpResponse


def homePage(request):
    total_projects = Project.objects.all().count()
    total_bugs = Bug_table.objects.all().count()
    total_pro3 = Bug_table.objects.filter(project_id=3).count()
    return render(request, "index.html",
                  {"total_projects": total_projects, "total_bugs": total_bugs, "total_bug3": total_pro3})


def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("form saved")
                return redirect("/summary")
            except:
                pass
        else:
            return HttpResponse("Data is not correct")
    else:
        form = ProjectForm()
    return render(request, "add_project.html", {'form': form})


def new_bug(request, id):
    if request.method == "POST":
        form = Bug_tableForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/summary")
            except:
                pass
        else:
            return HttpResponse("Data is not correct")
    else:
        form = Bug_tableForm()
    return render(request, "add_bug.html", {'form': form, 'id': id})


def summary(request):
    form = Project.objects.all()
    return render(request, "summary.html", {'form': form})


def delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/summary")


def delete_bug(request, id):
    form = Bug_table.objects.get(id=id)
    form.delete()
    return redirect("/show_bugs")


def edit(request, id):
    form = Project.objects.get(id=id)
    return render(request, "edit.html", {'form': form})


def update(request, id):
    form = Project.objects.get(id=id)
    form = ProjectForm(request.POST, instance=form)
    if form.is_valid():
        form.save()
        return redirect("/summary")
    return render(request, "edit.html", {'form': form})


def show_bugs(request, id=0):
    # bugs = Bug_table.objects.all()
    bugs = Bug_table.objects.filter(project_id=id)
    return render(request, "show_bugs_info.html", {'bugs': bugs, 'req_id': id})
# <!--<a href="/add_new_bug">Add New Bug</a>-->

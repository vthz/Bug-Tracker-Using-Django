# map our url  to view function
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('add_new_project', views.new_project),
    path('add_new_bug/<int:id>', views.new_bug),
    path('delete/<int:id>', views.delete),
    path("edit/<int:id>", views.edit),
    path('update/<int:id>', views.update),
    path('summary', views.summary),
    path('see_project_bug/<int:id>', views.show_bugs),
    path('delete_bug/<int:id>', views.delete_bug),
    path('show_bugs',views.show_bugs)
]

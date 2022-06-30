from django.urls import path
from projects.views import (
    ProjectDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
)

urlpatterns = [
    path("", ProjectListView.as_view(), name="list_projects"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="show_project"),
    path("create/", ProjectCreateView.as_view(), name="create_project"),
    path(
        "<int:pk>/delete", ProjectDeleteView.as_view(), name="delete_project"
    ),
    path("<int:pk>/edit", ProjectUpdateView.as_view(), name="edit_project"),
]

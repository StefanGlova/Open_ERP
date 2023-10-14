from django.urls import path
from .views import ListIncidentsView, ViewIncidentView, AddIncidentView, EditIncidentView, DeleteIncidentView

urlpatterns = [
    path("incidents/", ListIncidentsView.as_view(), name="list_incidents"),
    path("incidents/<int:incident_id>/", ViewIncidentView.as_view(), name="view_incident"),
    path("incidents/add/", AddIncidentView.as_view(), name="add_incident"),
    path("incidents/<int:incident_id>/edit/", EditIncidentView.as_view(), name="edit_incident"),
    path("incidents/<int:incident_id>/delete/", DeleteIncidentView.as_view(), name="delete_incident"),
]
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

class ListIncidentsView(View):
    def get(self, request):
        response = requests.get("https://safetyapi-open-erp.onrender.com/api/incidents")
        incidents = response.json()
        return render(request, "health_safety_environment/home_incidents.html", {"incidents": incidents})


class ViewIncidentView(View):
    def get(self, request, incident_id):
        response = requests.get(
            f"https://safetyapi-open-erp.onrender.com/api/incidents/{incident_id}"
        )
        if response.status_code == 200:
            incident = response.json()
            return render(request, "view_incident.html", {"incident": incident})
        else:
            return JsonResponse({"error": "Incident not found"}, status=404)


class AddIncidentView(View):
    def get(self, request):
        return render(request, "health_safety_environment/add_incident.html")

    def post(self, request):
        data = {
            "incident_type": request.POST.get("incident_type"),
            "person_name": request.POST.get("person_name"),
            "incident_date": request.POST.get("incident_date"),
            "incident_time": request.POST.get("incident_time"),
            "witness_name": request.POST.get("witness_name"),
            "weather": request.POST.get("weather"),
            "light": request.POST.get("light"),
            "description": request.POST.get("description"),
        }

        response = requests.post(
            "https://safetyapi-open-erp.onrender.com/api/incidents", json=data
        )

        if response.status_code == 201:
            return JsonResponse({"message": "Incident added successfully"}, status=201)
        else:
            return JsonResponse(
                {"error": "Incident report failed. Check your data"}, status=400
            )


class EditIncidentView(View):
    def get(self, request, incident_id):
        response = requests.get(
            f"https://safetyapi-open-erp.onrender.com/api/incidents/{incident_id}"
        )
        if response.status_code == 200:
            incident = response.json()
            return render(request, "edit_incident.html", {"incident": incident})
        else:
            return JsonResponse({"error": "Incident not found"}, status=404)

    def post(self, request, incident_id):
        data = {
            "incident_type": request.POST.get("incident_type"),
            "person_name": request.POST.get("person_name"),
            "incident_date": request.POST.get("incident_date"),
            "incident_time": request.POST.get("incident_time"),
            "witness_name": request.POST.get("witness_name"),
            "weather": request.POST.get("weather"),
            "light": request.POST.get("light"),
            "description": request.POST.get("description"),
        }

        response = requests.put(
            f"https://safetyapi-open-erp.onrender.com/api/incidents/{incident_id}",
            json=data,
        )

        if response.status_code == 201:
            return JsonResponse(
                {"message": "Incident updated successfully"}, status=201
            )
        else:
            return JsonResponse(
                {"error": "Incident update failed. Check your data"}, status=400
            )


class DeleteIncidentView(View):
    def post(self, request, incident_id):
        response = requests.delete(
            f"https://safetyapi-open-erp.onrender.com/api/incidents/{incident_id}"
        )

        if response.status_code == 201:
            return JsonResponse(
                {"message": "Incident deleted successfully"}, status=201
            )
        else:
            return JsonResponse({"error": "Incident deletion failed"}, status=400)

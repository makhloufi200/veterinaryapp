from django.urls import path

from medicine import views as medicine_view


urlpatterns = [
    path('medicine/', medicine_view.list_medecine, name='list_medecine'),
	path('medicine/add/', medicine_view.create_medecine, name="create_medecine"),
	path('medicine/<int:medicine_id>/', medicine_view.datail_medecine, name='datail_medecine'),
	path('medicine/<int:medicine_id>/edit/', medicine_view.update_medecine, name="update_medecine"),
    path('medicine/<int:medicine_id>/delete/', medicine_view.medecine_delete, name="medecine_delete"),
    
]
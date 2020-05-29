from django.urls import path

from animal import views as animal_view


urlpatterns = [
    path('animal/', animal_view.list_animal, name='list_animal'),
	path('animal/add/', animal_view.create_animal, name="create_animal"),
	path('animal/<int:animal_id>/', animal_view.datail_animal, name='datail_animal'),
	path('animal/<int:animal_id>/edit/', animal_view.update_animal, name="update_animal"),
    path('animal/<int:animal_id>/delete/', animal_view.animal_delete, name="animal_delete"),
	path('animal/export', animal_view.export_animal_csv, name='export_animal_csv'),
    
]
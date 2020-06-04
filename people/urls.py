from django.urls import path
from people import views as people_view
from . import views

urlpatterns = [
    path('people/', people_view.list_people, name='list_people'),
	path('people/add/', people_view.create_people, name="create_people"),
	path('people/<int:people_id>/', people_view.datail_people, name='datail_people'),
	path('people/<int:people_id>/edit/', people_view.update_people, name="update_people"),
    path('people/<int:people_id>/delete/', people_view.people_delete, name="people_delete"),
	path('people/export', people_view.export_costomer_csv, name='export_costomer_csv'),
    
]
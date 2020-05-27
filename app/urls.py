from django.urls import path

from app import views as app_view

urlpatterns = [
	path('export/', app_view.exportdatabase, name='export_database'),
	path('import/', app_view.importdatabase, name='import_database'),
    
]
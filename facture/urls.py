from django.urls import path

from facture import views as facture_view


urlpatterns = [
    path('facture/', facture_view.list_facture, name='list_facture'),
	path('facture/add/', facture_view.create_facture, name="create_facture"),
	path('facture/<int:facture_id>/', facture_view.datail_facture, name='datail_facture'),
	path('facture/<int:facture_id>/edit/', facture_view.update_facture, name="update_facture"),
    path('facture/<int:facture_id>/delete/', facture_view.facture_delete, name="facture_delete"),
	#-----------------------------------------------------------------------------------------------
	path('facture_medecine/', facture_view.list_facture_medecine, name='list_facture_medecine'),
	path('facture/<int:facture_id>/medecine', facture_view.create_facture_medecine, name="create_facture_medecine"),
	path('facture/<int:facture_id>/<int:medecine_id>/', facture_view.facture_medecine_delete, name="facture_medecine_delete"),
    
]
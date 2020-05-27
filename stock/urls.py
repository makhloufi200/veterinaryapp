from django.urls import path

from stock import views as stock_view


urlpatterns = [
    path('stock/', stock_view.list_stock, name='list_stock'),
	path('stock/add/', stock_view.create_stock, name="create_stock"),
	path('stock/<int:stock_id>/', stock_view.datail_stock, name='datail_stock'),
	path('stock/<int:stock_id>/edit/', stock_view.update_stock, name="update_stock"),
    path('stock/<int:stock_id>/delete/', stock_view.stock_delete, name="stock_delete"),
    
]
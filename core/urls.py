from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('product/<int:product_id>', views.product, name='product'),
    path('substitute/<int:product_id>', views.substitute, name='substitute'),
    path('save/<int:product_id>/<int:prod_id>', views.save, name='save'),
    path('favorite', views.favorite, name='favorite'),
    path('delete/<int:fav>', views.delete, name='delete'),
]

app_name = 'core'

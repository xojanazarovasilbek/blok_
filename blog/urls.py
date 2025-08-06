from django.urls import path
from .views import home_page, detail_view, set_rating

urlpatterns = [
    path('', home_page, name='home'),
    path('detail/<pk>/', detail_view, name='detail'),
    path('rating/<value>/<id>/', set_rating, name='set_rating')
]

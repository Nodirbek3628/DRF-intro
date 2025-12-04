from django.urls import path
from .views import ItemViewSets

urlpatterns = [
    path('items/',ItemViewSets.as_view({'get':'list','post':'create'})),
    path('items/<int:pk>/',ItemViewSets.as_view({'get':'list','put':'update','delete':'destroy'}))
]

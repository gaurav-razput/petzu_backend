from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pets import views

urlpatterns = [
    path('', views.PetList.as_view()),
    path('<int:pk>/', views.PetViewDetails.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from .views import AnimalListAPIView

urlpatterns = [
   path('animal/', AnimalListAPIView.as_view()),
   #path('animal/<int:pk>/', AnimalDetail.as_view()),
   #path('', showanimal),

]

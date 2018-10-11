from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bbs import views


urlpatterns = [
    path('', views.EventsList.as_view()),
    path('<int:pk>/', views.EventsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


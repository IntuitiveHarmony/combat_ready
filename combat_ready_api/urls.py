from django.urls import path
from . import views

urlpatterns = [
    path('api/matches', views.MatchesList.as_view(), name='matches_list'), 
    path('api/matches/<int:pk>', views.MatchesDetail.as_view(), name='matches_detail'),
]

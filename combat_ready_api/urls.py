from django.urls import path
from . import views

urlpatterns = [
    path('api/matches', views.MatchesList.as_view(), name='matches_list'), 
    path('api/matches/<int:pk>', views.MatchesDetail.as_view(), name='matches_detail'),
    path('api/Stage', views.StageList.as_view(), name='Stage_list'), 
    path('api/Stage/<int:pk>', views.StageDetail.as_view(), name='Stage_detail'),
]




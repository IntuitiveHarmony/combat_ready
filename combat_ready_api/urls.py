from django.urls import path
from . import views

urlpatterns = [
    path('api/combatant', views.CombatantList.as_view(), name='combatant_list'), 
    path('api/combatant/<int:pk>', views.CombatantDetail.as_view(), name='combatant_detail'),
]

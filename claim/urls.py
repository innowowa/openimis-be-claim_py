from django.urls import path
from claim import views

urlpatterns = [
    path('print/', views.print, name='print'),
    path('attach/', views.attach, name='attach'),
    path('get-new-claim-code/', views.get_new_claim_code, name='get-new-claim-code')
]

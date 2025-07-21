from django.urls import path
from APP.views import *

urlpatterns = [
    path('create', create_income_view, name='create'),
    path('edit/<int:pk>', edit_income_view, name='edit'),
    path('delete/<int:pk>', delete_income_view, name='delete'),
    path('income_list', income_list_view, name='income_list'),
]
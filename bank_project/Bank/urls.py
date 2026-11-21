

from django.urls import path
from .views import (
    HomeView,
    CustomLoginView,
    CustomLogoutView,
    RegisterView,
    ProfileView,
    ClientListView,
    AccountListView,
    CardListView,
    TransactionListView,
)

app_name = 'Bank'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('accounts/', AccountListView.as_view(), name='accounts'),
    path('cards/', CardListView.as_view(), name='cards'),
    path('transactions/', TransactionListView.as_view(), name='transactions'),
]

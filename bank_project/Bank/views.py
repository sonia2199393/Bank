
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Client, BankAccount, BankCard, Transaction


# Головна сторінка
class HomeView(TemplateView):
    template_name = 'Bank/home.html'


# Авторизація
class CustomLoginView(LoginView):
    template_name = 'Bank/login.html'
    redirect_authenticated_user = True


# Вихід з акаунта
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('Bank:login')


# Реєстрація
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'Bank/register.html'
    success_url = reverse_lazy('Bank:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


# Профіль
class ProfileView(TemplateView):
    template_name = 'Bank/profile.html'


# Список клієнтів
class ClientListView(ListView):
    model = Client
    template_name = 'Bank/clients.html'
    context_object_name = 'clients'


# Список рахунків
class AccountListView(ListView):
    model = BankAccount
    template_name = 'Bank/accounts.html'
    context_object_name = 'accounts'


# Список карток
class CardListView(ListView):
    model = BankCard
    template_name = 'Bank/cards.html'
    context_object_name = 'cards'


# Список транзакцій
class TransactionListView(ListView):
    model = Transaction
    template_name = 'Bank/transactions.html'
    context_object_name = 'transactions'

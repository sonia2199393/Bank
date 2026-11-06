
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BankAccount(models.Model):
    CURRENCY_CHOICES = [
        ('UAH', 'Гривня'),
        ('USD', 'Долар'),
        ('EUR', 'Євро'),
    ]

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    account_number = models.CharField(max_length=29, unique=True)
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='UAH'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.client}"


class BankCard(models.Model):
    account = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        related_name='cards'
    )
    card_number = models.CharField(max_length=16, unique=True)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Картка ****{self.card_number[-4:]}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Поповнення'),
        ('withdraw', 'Зняття коштів'),
        ('transfer', 'Переказ'),
    ]

    account = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount}"

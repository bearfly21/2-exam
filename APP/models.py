from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_income')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(User, related_name="income_category", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"
    
    class Meta:
        verbose_name = ("Income")
        verbose_name_plural = ("Incomes")
    
class Expense(models.Model):
    user = models.ForeignKey(User, related_name="user_expense", on_delete=models.CASCADE)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.ForeignKey(Category, related_name="user_category", on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"
    
    class Meta:
        verbose_name = ("Expense")
        verbose_name_plural = ("Expenses")





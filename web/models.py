from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} | {self.amount} | {self.date}"


class Income(models.Model):
    text = models.TextField()
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text} | {self.amount} | {self.date}"

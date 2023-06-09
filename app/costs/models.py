from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class FixedCosts(models.Model):
    user = models.ForeignKey(User, related_name="fixed_costs", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sume = models.DecimalField(max_digits=11, decimal_places=2)
    notes = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name_plural = "Fixed Costs"
        ordering = ["-sume"]

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})


class VariableCosts(models.Model):
    user = models.ForeignKey(
        User, related_name="variable_costs", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    sume = models.DecimalField(max_digits=11, decimal_places=2)
    notes = models.CharField(max_length=300, blank=True)
    date = models.DateField(default=now)

    class Meta:
        verbose_name_plural = "Variable Costs"
        ordering = ["date"]

    def __str__(self) -> str:
        return self.title


class Income(models.Model):
    user = models.ForeignKey(User, related_name="income", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sume = models.DecimalField(max_digits=11, decimal_places=2)
    notes = models.CharField(max_length=300, blank=True)
    date = models.DateField(default=now)

    class Meta:
        verbose_name_plural = "Income"
        ordering = ["date"]

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})

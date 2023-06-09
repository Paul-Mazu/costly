from django.contrib import admin
from .models import FixedCosts, VariableCosts, Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = ("title", "sume", "date")


class FixedCostsAdmin(admin.ModelAdmin):
    list_display = ("title", "sume")


class VariableCostsAdmin(admin.ModelAdmin):
    list_display = ("title", "sume", "date")


admin.site.register(FixedCosts, FixedCostsAdmin)
admin.site.register(VariableCosts, VariableCostsAdmin)
admin.site.register(Income, IncomeAdmin)

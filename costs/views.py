from calendar import month
from django.shortcuts import render
from .models import Income, FixedCosts, VariableCosts
from django.db.models import DateField
import calendar
from datetime import datetime


def listView(request, requested_year):
    distinct_months = (
        VariableCosts.objects.filter(date__year=requested_year)
        .values_list("date__month", flat=True)
        .distinct()
        .order_by("date__month")
    )
    distinct_months = [
        calendar.month_name[month_number] for month_number in distinct_months
    ]

    return render(
        request,
        "costs/months-list.html",
        context={"months": distinct_months, "requested_year": requested_year},
    )


def detailedListView(request, requested_year, requested_month):
    month_number = datetime.strptime(requested_month, "%B").month
    variable_costs = VariableCosts.objects.filter(
        date__year=requested_year, date__month=month_number
    )

    return render(
        request, "costs/month-details.html", context={"variable_costs": variable_costs}
    )

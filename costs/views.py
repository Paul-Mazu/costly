from calendar import month
from django.shortcuts import render
from .models import Income, FixedCosts, VariableCosts


def listView(request, chosen_year):
    dates = VariableCosts.objects.values_list("date", flat=True).distinct()
    distinct_months = {}
    for dat in dates:
        month, year = dat.strftime("%B"), dat.strftime("%Y")
        if year not in distinct_months:
            distinct_months[year] = {month}
        else:
            distinct_months[year].add(month)
    months = distinct_months.get(chosen_year)

    return render(request, "costs/months-list.html", context={"months": months})


def detailedListView(request, chosen_month):
    pass

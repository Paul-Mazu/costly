from .models import VariableCosts


def available_years(request):
    dates = VariableCosts.objects.values_list("date", flat=True).distinct()
    distinct_years = {dat.strftime("%Y") for dat in dates}
    distinct_years = sorted(list(distinct_years))
    return {"years": distinct_years}

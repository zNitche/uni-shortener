from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from core import models
from datetime import datetime
import calendar


@login_required()
@require_http_methods(["GET"])
def redirects_per_day(request, month_date):
    datetime_date = datetime.strptime(month_date, "%Y-%m")
    days_range = calendar.monthrange(datetime_date.year, datetime_date.month)
    data = {}

    for day in range(1, days_range[1] + 1):
        redirects = models.RedirectLog.objects.filter(date_redirected__month=datetime_date.month,
                                                      date_redirected__year=datetime_date.year,
                                                      date_redirected__day=day).all()

        data[day] = len(redirects)

    return JsonResponse(data)


@login_required()
@require_http_methods(["GET"])
def redirects_per_hour(request, day_date):
    datetime_date = datetime.strptime(day_date, "%Y-%m-%d")

    data = {}

    for hour in range(0, 24):
        redirects = models.RedirectLog.objects.filter(date_redirected__month=datetime_date.month,
                                                      date_redirected__year=datetime_date.year,
                                                      date_redirected__day=datetime_date.day,
                                                      date_redirected__hour=hour).all()

        data[hour] = len(redirects)

    return JsonResponse(data)

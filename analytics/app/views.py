from django.shortcuts import render
from app.models import Request
from django.db.models import Count, F
from django.db.models.functions import TruncDate


# Create your views here.

def home(request):
    context = {}
    # daily stats calc
    daily_unique_users = Request.objects\
        .values(date=TruncDate("dt"))\
        .annotate(
            daily_users=Count("ip_address", distinct=True),
            daily_requests=Count("ip_address", distinct=False)
        ).order_by("date")
    daily_user_labels = []
    daily_user_counts = []
    daily_request_counts = []
    for d in daily_unique_users:
        daily_user_labels += [d["date"].strftime('%Y-%m-%d')]
        daily_user_counts += [d["daily_users"]]
        daily_request_counts += [d["daily_requests"]]
    context['daily_user_labels'] = daily_user_labels
    context['daily_user_counts'] = daily_user_counts
    context['daily_request_counts'] = daily_request_counts

    # overall pageview stats

    url_labels = []
    url_values = []
    # requests_by_url = Request.objects.filter(url__isnull=False) .values("url").annotate(total_unique_visitors = Count("ip_address", unique=True)).filter(total_unique_visitors__gt=1).order_by("-total_unique_visitors")
    # for r in requests_by_url:
    #     url_labels += [r['url']]
    #     url_values += [r['total_unique_visitors']]
    # print(requests_by_url)
    # context['url_labels'] = url_labels
    # context['url_values'] = url_values


    print(daily_unique_users)
    return render(request, "home.html", context)

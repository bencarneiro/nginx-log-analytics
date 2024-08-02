from django.shortcuts import render
from app.models import Request
from django.db.models import Count, F
from django.db.models.functions import TruncDate


# Create your views here.

def home(request):
    context = {}
    daily_unique_users = Request.objects.values(date=TruncDate("dt")).annotate(daily_users=Count("ip_address", distinct=True)).order_by("date")
    labels = []
    daily_users = []
    for d in daily_unique_users:
        labels += [d["date"].strftime('%Y-%m-%d')]
        daily_users += [d["daily_users"]]
    context['daily_user_labels'] = labels
    context['daily_user_counts'] = daily_users
    print(daily_unique_users)
    return render(request, "home.html", context)

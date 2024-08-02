from django.core.management.base import BaseCommand
import datetime

from app.models import Request

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Request.objects.all().delete()
        f = open("/var/log/nginx/access.log", "r")
        for x in f:
            try:
                sections = x.split('"')
                ip = sections[0].split(" - - ")[0]
                date = sections[0].split("[")[1].split("]")[0]
                date = datetime.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S %z')
                try:
                    request_type = sections[1].split(" ")[0]
                    url = sections[1].split(" ")[1]
                    protocol = sections[1].split(" ")[2]
                except:
                    request_type = None
                    url = None
                    protocol = None
                status_code = sections[2].split(" ")[1]
                bytes_transferred = sections[2].split(" ")[2]
                referrer_url = sections[3]
                user_agent = sections[5]

                r = Request(
                    ip_address = ip,
                    dt = date,
                    request_type = request_type,
                    url = url,
                    protocol = protocol,
                    status_code = int(status_code),
                    bytes_transferred = int(bytes_transferred),
                    referrer_url = referrer_url,
                    user_agent = user_agent
                )
                r.save()
            except Exception as e:
                print(e)
                print(x)
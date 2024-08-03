from django.core.management.base import BaseCommand
import datetime

from app.models import Request

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        Request.objects.all().delete()
        filenames = [
            "access.log",
            "access.log.1",
            "access.log.2",
            "access.log.3",
            "access.log.4",
            "access.log.5",
            "access.log.6",
            "access.log.7",
            "access.log.8",
            "access.log.9",
            "access.log.10",
            "access.log.11",
            "access.log.12",
            "access.log.13",
            "access.log.14"
        ]
        for filepath in filenames:
            print(filepath)
            f = open("/var/log/nginx/" + filepath, "r")
            z = 0
            objects_to_insert = []
            # print(z)
            for x in f:
                # print(x)
                sections = x.split('"')
                date = sections[0].split("[")[1].split("]")[0]
                subsections = sections[1].split(" ")
                if len(subsections) != 3:
                    print(x)
                    continue
                if len(subsections[0]) > 8:
                    print(x)
                    continue
                    # subsections = [None, None, None]
                http_data = sections[2].split(" ")

                r = Request(
                    ip_address = sections[0].split(" - - ")[0],
                    dt =  datetime.datetime.strptime(date, '%d/%b/%Y:%H:%M:%S %z'),
                    request_type = subsections[0],
                    url = subsections[1],
                    protocol = subsections[2],
                    status_code = http_data[1],
                    bytes_transferred = http_data[2],
                    referrer_url = sections[3],
                    user_agent = sections[5]
                )
                objects_to_insert += [r]
                z += 1
                if z > 1000:
                    Request.objects.bulk_create(objects_to_insert)
                    objects_to_insert = []
                    z = 0
                    
            Request.objects.bulk_create(objects_to_insert)
            f.close()
                
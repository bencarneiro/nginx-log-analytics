from django.db import models

# Create your models here.

class Request(models.Model):
    ip_address = models.CharField(max_length=64, null=False, blank=False)
    dt = models.DateTimeField(null=False, blank=False)
    request_type = models.CharField(max_length=16, null=True, blank=True)
    url = models.CharField(max_length=512, null=True, blank=True)
    protocol = models.CharField(max_length=64, null=True, blank=True)
    status_code = models.PositiveSmallIntegerField(null=False, blank=False)
    bytes_transferred = models.PositiveIntegerField(null=True, blank=True)
    referrer_url = models.CharField(max_length=512, null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "request"    
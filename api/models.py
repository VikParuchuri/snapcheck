from django.db import models

CHARFIELD_MAX = 255

class PhoneRecord(models.Model):
    username = models.CharField(max_length=CHARFIELD_MAX, db_index=True)
    phone_number = models.CharField(max_length=CHARFIELD_MAX, db_index=True)
    location = models.CharField(max_length=CHARFIELD_MAX)

    class Meta:
        unique_together = (('username', 'phone_number'),)
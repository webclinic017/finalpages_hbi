from django.db import models
from django.utils import timezone

from django.conf import settings
User = settings.AUTH_USER_MODEL

DOCUMENT_CHOICES = (
    ("PROPOSAL", "proposal"),
    ("QUOTATION", "quotation"),
    ("E-PROOF", "e-proof"),
    ("POWERPOINT", "powerpoint"),
    ("BROCHURE", "brochure"),
    ("CERTIFICATE", "certificate"),
    ("MANUAL", "manual"),
    ("MISCELLANEOUS", "miscellaneous"),
)

COUNTRY_CHOICES = (
    ("ALL", "All"),
    ("BRUNEI", "Brunei"),
    ("CAMBODIA", "Cambodia"),
    ("HONG KONG", "Hong Kong"),
    ("INDONESIA", "Indonesia"),
    ("LAOS", "Laos"),
    ("MALAYSIA", "Malaysia"),
    ("MONGOLIA", "Mongolia"),
    ("MYANMAR", "Myanmar"),
    ("PAKISTAN", "Pakistan"),
    ("PHILIPPINES", "Philippines"),
    ("SINGAPORE", "Singapore"),
    ("THAILAND", "Thailand"),
    ("VIETNAM", "Vietnam"),
)

class Listing(models.Model):
    title = models.CharField(max_length=100)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=DOCUMENT_CHOICES, default="miscellaneous")
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, default="any")
    docfile = models.FileField(upload_to='documents/docfiles/%Y/%m/%d/')
    cover = models.ImageField(upload_to='documents/covers/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
      return self.title

    def delete(self, *args, **kwargs):
      self.pdf.delete()
      self.cover.delete()
      super().delete(*args, **kwargs)

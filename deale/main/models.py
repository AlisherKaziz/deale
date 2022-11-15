from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=50, name="", default="", )
    description = models.TextField()
    phone = PhoneNumberField(null=False, blank=False, unique=False, region='RU')
    address = models.TextField(help_text="В google maps найти вашу компанию и вставить src ссылку")

    def __str__(self):
        return self.name

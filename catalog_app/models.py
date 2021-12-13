from django.core.validators import RegexValidator
from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Vehicle(models.Model):
    driver_id = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        related_name='cars',
        blank=True,
        null=True
    )
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    plate_number = models.CharField(
        max_length=255,
        unique=True,
        validators=[RegexValidator(r'[А-Я]{2} \d{4} [А-Я]{2}')]
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.plate_number} - {self.model}'
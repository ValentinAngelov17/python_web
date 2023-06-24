from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django import forms


# Create your models here.
def letter_validator(value):
    if value[0].isalpha():
        pass
    else:
        raise ValidationError("Your name must start with a letter!")


def letter_validator_fruit(value):
    if value[0].isalpha():
        pass
    else:
        raise ValidationError("Fruit name should contain only letters!")


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        verbose_name='First Name',
        validators=[validators.MinLengthValidator(2), letter_validator],

    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        verbose_name='Last Name',
        validators=[validators.MinLengthValidator(1), letter_validator],
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )
    password = models.CharField(
        max_length=40,
        validators=[validators.MinLengthValidator(8)],
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='image URL'
    )
    age = models.IntegerField(
        blank=True,
        null=True,
        default=18,
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=[validators.MinLengthValidator(2), letter_validator_fruit],

    )
    image_url = models.URLField(
        verbose_name='Image URL',
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )

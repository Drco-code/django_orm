from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower


from django.utils.translation import gettext_lazy as _


# Create your models here.

"""
Restaurant Management System
1. Create a model for a User
2. Create a model for a Restaurant
3. Create a model for a Rating
"""



def validate_restaurant_name_begins_with(value):
    if not value.startswith("a"):
        raise ValidationError(
            "Restaurant Name must start with a"
        )
    

class Restaurant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(_("Restaurant Name"), max_length=100, validators=[validate_restaurant_name_begins_with])
    website = models.URLField(_("Restaurant Website"), default='', max_length=200)
    date_opened = models.DateField(_("Restaurant Open Date"))
    latitude = models.FloatField(_("Restaurant Latitude"), validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(_("Restaurant Longitude"), validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(
        _("Restaurant Type"), 
        max_length=2, 
        choices=TypeChoices.choices,  
        blank=True,
        null=True
    )

    class Meta:
        ordering = [Lower('name')]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print(self._state.adding)
        super().save(*args, **kwargs)
    
    
class Rating(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, verbose_name=_("Restaurant"),related_name="ratings"
                                   ,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(_("User Rating"),
            validators=[MinValueValidator(1), MaxValueValidator(5)]
            )

    def __str__(self):
        return f"Rating: {self.rating}"
    
class Sales(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name=_("Restaurant"), related_name="sales", on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(_("Restaurant Income"), max_digits=8, decimal_places=2)
    datetime = models.DateTimeField(_("Date and Time of Sale"))

    def __str__(self):
        return f"INCOME: {self.income} "
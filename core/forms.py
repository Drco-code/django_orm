from django import forms
from core.models import Rating, Restaurant


# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ['user','restaurant', 'rating']
#         widgets = {
#             "restaurant": forms.Select(attrs={"class": "form-control"}),
#             "rating": forms.NumberInput(attrs={"class": "form-control"}),
#         }

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'latitude', 'longitude', 'restaurant_type']


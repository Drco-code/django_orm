from core.models import Restaurant, User, Rating, Sales
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower

def run():

    # METHOD 1
    """

    restaurant = Restaurant()
    
    restaurant.name = "My Itlaian Restaurant"
    restaurant.latitude = 50.2
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    restaurant.save()

    if(restaurant.save):
        print(f"{restaurant.name} Restaurant saved successfully")
    else:
        print("Error saving restaurant")

     """   
    
    # METHOD 2
    """
    Restaurant.objects.create(
        name="Pizza Shop",
        date_opened =timezone.now(),
        restaurant_type = Restaurant.TypeChoices.ITALIAN,
        latitude = 50.2,
        longitude = 50.2
    )
    """


    # QUERYING DATA

    """

    restaurants = Restaurant.objects.last()
    restaurants_number = Restaurant.objects.count()

    print(restaurants, restaurants_number)
    """

    """
    restaurant = Restaurant.objects.first()
    user = User.objects.first()

    Rating.objects.create(
        user = user,
        restaurant = restaurant,
        rating = 3,
    )

    print(connection.queries)
    """

    
    """
    rating1 = Rating.objects.filter(rating__gte=3)
    rating2= Rating.objects.exclude(rating=5)
    print(rating1, rating2)

    pprint(connection.queries)

    restaurant = Restaurant.objects.first()
    restaurant.name = "abcddefggff"
    restaurant.save()

    pprint(restaurant.name)
    """
    """
    restaurant = Restaurant.objects.first()

    Sales.objects.create(
        restaurant = restaurant,
        income = 2.33,
        datetime = timezone.now()
    )

    Sales.objects.create(
        restaurant = restaurant,
        income = 5.33,
        datetime = timezone.now()
    )

    Sales.objects.create(
        restaurant = restaurant,
        income = 8.33,
        datetime = timezone.now()
    )
    """
    """

    restaurant = Restaurant.objects.first()


    print(restaurant.ratings.all())
    print(restaurant.sales.all())

    pprint(connection.queries)

    """

    """
    # GET OR CREATE

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating, created = Rating.objects.get_or_create(
        user = user,
        restaurant = restaurant,
        rating = 4
    )
    
    if created:
        # send email
        print("Rating created")
        print(rating)
    else:
        # send welcome message
        print("Rating already exists")
        print(rating)

    pprint(connection.queries)

    """

    """

    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    Rating.objects.create(
        user = user,
        restaurant = restaurant,
        rating = 9
    )

    rating = Rating()
    rating.user = user
    rating.restaurant = restaurant
    rating.rating = 5

    rating.full_clean()
    rating.save()
    """
    """

    restaurant = Restaurant.objects.first()
    print(restaurant.name)

    restaurant.name = "New Restaurant Name"

    restaurant.save(update_fields=['name'])

    pprint(connection.queries)
    """

    """
    restaurant = Restaurant()
    restaurant.name = "My Italian Restaurant #2"
    restaurant.date_opened = timezone.now()
    restaurant.latitude = 50.2
    restaurant.longitude = 50.2
    restaurant.restaurant_type = Restaurant.TypeChoices.ITALIAN

    restaurant.save()

    print(connection.queries)
    """
    """
    restaurant = Restaurant.objects.filter(name__startswith="P")
    pprint(restaurant)
    print("\n")

    print(restaurant.update(
        date_opened = timezone.now() - timezone.timedelta(days=365),
        website='https://last.com'
    ))

    pprint(connection.queries)
    """
    # FILTER DOWN TO ONLY CHINEESE RESTAURANTS


    """
    chinese = Restaurant.TypeChoices.CHINESE
    indian = Restaurant.TypeChoices.INDIAN
    mexican = Restaurant.TypeChoices.MEXICAN

    check_types = [chinese, indian, mexican]

    restaurant = Restaurant.objects.filter(restaurant_type=chinese, name__startswith="C") #AND
    print(restaurant)
    print(restaurant.exists())
    
    restaurants = Restaurant.objects.filter(restaurant_type__in=check_types) #IN

    print(restaurants)

    """

    restaurant = Restaurant.objects.order_by('date_opened')[2:7]
    print(restaurant)

    

    pprint(connection.queries)
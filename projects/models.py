from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    location = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default='noprofil.jpg')
    password1 = models.CharField(max_length=200, null=True, blank=True)
    password2 = models.CharField(max_length=200, null=True, blank=True)


    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.id)
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
class ListProperty(models.Model):
    
    Bachelers_Allowed = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    Independent = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
  
    By = (
        ('owner', 'owner'),
        ('broker', 'broker'),
    )
    
    
    Furnished_Flat = (
        ('Furnished', 'Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Non-Furnished', 'Non-Furnished')
    )
    
    Balcony = (
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )
    
    Parking = (
        ('Available', 'Available'),
        ('Not-Available', 'Not-Available')
    )
    
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, blank=True, null=True)
    property_name = models.CharField(max_length=50, null=True, blank=True)
    property_image = models.ImageField(null=True, blank=True, default='ds2.jpg')
    Rent = models.IntegerField(null=True, blank=True)
    security_deposit = models.IntegerField(null=True, blank=True)
    no_of_bedroom = models.IntegerField(default=1)
    no_of_hall = models.IntegerField(default=1)
    no_of_kitchen = models.IntegerField(default=1)
    no_of_bathroom = models.IntegerField(default=1)
    property_location = models.CharField(max_length=200, blank=True, null=True)
    contact_detail = models.IntegerField()
    description = models.TextField()
    bachelers_allowed = models.CharField(max_length=100, choices=Bachelers_Allowed, default='Yes')
    furnished = models.CharField(max_length=100, choices=Furnished_Flat, default="Non-Furnished")
    balcony = models.CharField(max_length=100, choices=Balcony, default="Not-Available")
    parking = models.CharField(max_length=100, choices=Parking, default="Not-Available")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    independent = models.CharField(max_length=100, choices=Independent)
    by = models.CharField(max_length=100, choices=By, default='owner')
    
    
    @property
    def imageURL(self):
        try:
            url = self.property_image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return str(self.id)
    

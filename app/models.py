from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICE=(
("Andhra Pradesh","Andhra Pradesh"),
("Arunachal Pradesh ","Arunachal Pradesh "),
("Assam","Assam"),
("Bihar","Bihar"),
("Chhattisgarh","Chhattisgarh"),
("Goa","Goa"),
("Gujarat","Gujarat"),
("Haryana","Haryana"),
("Himachal Pradesh","Himachal Pradesh"),
("Jammu and Kashmir ","Jammu and Kashmir "),
("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),
("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),
("Maharashtra","Maharashtra"),
("Manipur","Manipur"),
("Meghalaya","Meghalaya"),
("Mizoram","Mizoram"),
("Nagaland","Nagaland"),
("Odisha","Odisha"),
("Punjab","Punjab"),
("Rajasthan","Rajasthan"),
("Sikkim","Sikkim"),
("Tamil Nadu","Tamil Nadu"),
("Telangana","Telangana"),
("Tripura","Tripura"),
("Uttar Pradesh","Uttar Pradesh"),
("Uttarakhand","Uttarakhand"),
("West Bengal","West Bengal"),
("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
("Chandigarh","Chandigarh"),
("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
("Daman and Diu","Daman and Diu"),
("Lakshadweep","Lakshadweep"),
("National Capital Territory of Delhi","National Capital Territory of Delhi"),
("Puducherry","Puducherry")
)


# Create your models here.
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICE, max_length=50)

    def __str__(self):
        return str(self.id)


CATAGORY_CHOICE=(
("M","Mobile"),
("L","Laptop"),
("TW","Top Wear"),
("BW","Bottom Wear"),
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=50)
    catagory=models.CharField(choices=CATAGORY_CHOICE,max_length=2)
    product_image=models.ImageField(upload_to='myimage')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


STATUS_CHOICE=(
("Accepted","Accepted"),
("Packed","Packed"),
("On The Way","On The Way"),
("Delivered","Delivered"),
("Cancel","Cancel"),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=STATUS_CHOICE,max_length=50,default='pending')




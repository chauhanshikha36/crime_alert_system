from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'

class Product(models.Model):
    pro_name = models.CharField(max_length=30)
    pro_des = models.TextField()
    img_name= models.CharField(max_length=30)

    class Meta:
        db_table = 'product'
class City(models.Model):
    city_name = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'City'
class Area(models.Model):
	area_name = models.CharField(max_length=30)
	city = models.ForeignKey(City,on_delete=models.CASCADE)
    
	class Meta:
		db_table = 'Area'

class Inquiry(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    message=models.TextField()

    class Meta:
        db_table='inquiry'



class Profile(models.Model):
    contact=models.BigIntegerField()
    address=models.TextField()
    area= models.ForeignKey(Area, on_delete=models.CASCADE, default='')
    # relatives= models.ForeignKey(Relatives, on_delete=models.CASCADE,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.CharField(max_length=30, default='')
    class Meta:
        db_table='profile'

class Post(models.Model):
    post_description=models.TextField()
    p_date = models.DateField(auto_now_add=True)
    file_name=models.CharField(max_length=255)
    area= models.ForeignKey(Area, on_delete=models.CASCADE, default='')
    category= models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE, default='')
    class Meta:
        db_table='post'

class Feedback(models.Model):
    message=models.TextField()
    rating=models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='feedback'

class Quickcontact(models.Model):
    email = models.CharField(max_length=30)
    message=models.TextField()

    class Meta:
        db_table='Quickcontact'


class Comment(models.Model):
    msg  = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    class Meta:
        db_table='comment'

class Likes(models.Model):
    user_like=models.IntegerField()
    user_dislike=models.IntegerField()
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table='likes'

class Report(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        db_table='report'

# class Total(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     class Meta:
#         db_table='total'


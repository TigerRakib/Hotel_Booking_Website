from django.db import models

# Create your models here. 
class company(models.Model):
    company_name=models.CharField(max_length=255)
    content=models.TextField()
    phone=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    email=models.EmailField()
    opening_hours=models.CharField(max_length=255)
    video_link=models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.company_name
class why_us(models.Model):
    icon=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.title
class stats(models.Model):
    category=models.CharField(max_length=255)
    number=models.IntegerField()
    def __str__(self):
        return self.category
class food_type(models.Model):
    type=models.CharField(max_length=255)
    def __str__(self):
        return self.type

class starters(models.Model):
    pic=models.CharField(max_length=255,blank=True,null=True)
    food_name=models.CharField(max_length=255)
    food_ingredients=models.CharField(max_length=255)
    price=models.IntegerField()
    def __str__(self):
        return self.food_name
class breakfast(models.Model):
    pic=models.CharField(max_length=255,blank=True,null=True)
    food_name=models.CharField(max_length=255)
    food_ingredients=models.CharField(max_length=255)
    price=models.IntegerField()
    def __str__(self):
        return self.food_name
class lunch(models.Model):
    pic=models.CharField(max_length=255,blank=True,null=True)
    food_name=models.CharField(max_length=255)
    food_ingredients=models.CharField(max_length=255)
    price=models.IntegerField()
    def __str__(self):
        return self.food_name
class dinner(models.Model):
    pic=models.CharField(max_length=255,blank=True,null=True)
    food_name=models.CharField(max_length=255)
    food_ingredients=models.CharField(max_length=255)
    price=models.IntegerField()
    def __str__(self):
        return self.food_name
class testimonial(models.Model):
    picture=models.CharField(max_length=255,blank=True,null=True)
    name=models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    rating=models.IntegerField()
    description=models.TextField()
    def __str__(self):
        return self.name 
class event(models.Model):
    picture=models.CharField(max_length=255,blank=True,null=True)
    event=models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return self.event
class professionals(models.Model):
    picture=models.CharField(max_length=255,blank=True,null=True)
    name=models.CharField(max_length=255,blank=True,null=True)
    designation=models.CharField(max_length=255)
    description=models.TextField()
    def __str__(self):
        return self.designation
class galleries(models.Model):
    picture=models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)
class contact_form(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    is_success=models.BooleanField()
    is_error=models.BooleanField()
    action_time=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.email
class booking_info(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    people=models.IntegerField()
    message=models.TextField()
    is_success=models.BooleanField(blank=True,null=True)
    is_error=models.BooleanField(blank=True,null=True)
    action_time=models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.email
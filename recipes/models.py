from django.db import models
import datetime 
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    typ = models.CharField(max_length=20, null=True) #gromada
    gromada = models.CharField(max_length=20, null=True) #klasa
    rzad = models.CharField(max_length=20, null=True) #rząd
    def __str__(self):
        return self.name
    
class Difficulty(models.TextChoices):
    EASY = 'ES', ('Easy')
    MEDIUM = 'MD', ('Medium')
    HARD = 'HD', ('Hard')
    
class Ingredients(models.Model):
    nazwa=models.CharField(max_length=20, blank=True, null=True)
    is_healthy = models.BooleanField(null=True, default='0')
    is_fattening = models.BooleanField(null=True, default='0')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.nazwa
    pass


class Recipe(models.Model):
    title = models.CharField(max_length=150, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    steps = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredients)
    prep_time = models.DurationField()
    servings = models.IntegerField()
    difficulty = models.CharField(max_length=6, 
                                  choices=Difficulty.choices,
                                  default=Difficulty.EASY)
    author = models.CharField(max_length=35, blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(null = True, upload_to = 'images')
    
    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Comment(models.Model):
    recipe = models.ForeignKey('Recipe',null=True, to_field='title', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
class Advice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, primary_key=True)
    author = models.CharField(max_length=35, blank=True, null=True) 
    title = models.CharField(max_length=150)
    text = models.TextField()
    ScientificallyProven = models.BooleanField(null=True, default='0')
    def __str__(self):
        return self.title
    
class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=35, blank=True, null=True) 
    description = models.TextField()
    def __str__(self):
        return self.title

class BadThings(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    def __str__(self):
        return self.name    
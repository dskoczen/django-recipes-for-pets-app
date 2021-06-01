from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredients, Category, Comment, Advice, Book, BadThings

admin.site.register(Recipe)
admin.site.register(Ingredients)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Advice)
admin.site.register(Book)
admin.site.register(BadThings)


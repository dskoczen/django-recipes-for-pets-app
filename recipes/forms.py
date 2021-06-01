from .models import Comment, Category, Ingredients, Recipe, Comment, Advice, Book, BadThings
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'typ', 'gromada', 'rzad']
        
class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['nazwa', 'is_healthy', 'is_fattening', 'category']
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'steps', 'ingredients', 'prep_time', 'servings', 'difficulty', 'author', 'pub_date', 'image']
        
class AdviceForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ['category', 'author', 'title', 'text', 'ScientificallyProven']
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category','title','author','description']
        
class WarningForm(forms.ModelForm):
    class Meta:
        model = BadThings
        fields = ['category','name','description']
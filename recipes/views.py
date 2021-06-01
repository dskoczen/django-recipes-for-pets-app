from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Recipe, Category, Comment, Ingredients, Book, Advice, BadThings
from .forms import CommentForm,AdviceForm, WarningForm, CategoryForm, IngredientsForm, RecipeForm, BookForm
from flask import Flask, render_template, request, redirect

class IndexView(generic.ListView):
     context_object_name = 'cat_list'
     template_name = 'recipes/index.html'
     def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.ListView):
    model = Recipe
    template_name = 'recipes/detail.html'
    context_object_name = 'recipe_list'
    
    def get_queryset(self):
        return Recipe.objects.filter(category_id=self.kwargs['pk'])

def book(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'recipes/book.html', context)

def advice(request):
    advice_list = Advice.objects.all()
    context = {'advice_list': advice_list}
    return render(request, 'recipes/advice.html', context)

def warnings(request):
    warning_list = BadThings.objects.all()
    context = {'warning_list': warning_list}
    return render(request, 'recipes/warnings.html', context)

def comments(request):
    com_list = Comment.objects.all()
    context = {'com_list': com_list}
    return render(request, 'recipes/comments.html', context)

    
class ResultsView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/results.html'
    context_object_name = 'recipe_det'
    
def add_comment_to_recipe(request):
    #if request.method == "POST":
    formularz = CommentForm(request.POST or None)
    if formularz.is_valid():
            #comment = form.save(commit=False)
            #comment.recipe = recipe
            formularz.save()
            #return redirect('post_detail', pk=recipe.pk)
    #else:
        #form = CommentForm()
    return render(request, 'recipes/add_comment_to_recipe.html', {'form': formularz})
  
class CommentView(generic.ListView):
    model = Comment
    template_name = 'recipes/comments.html'
    context_object_name = 'com_list'
    
    def get_queryset(self):
        return Comment.objects.filter(recipe_id=self.kwargs['pk'])
    
def formCategory(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def editCategory(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, request.FILES or None, instance = cat)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/edit.html', {'form': form})
    
def delCategory(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        cat.delete()
    return render(request, 'recipes/delete.html', {'category_id': category_id})

def formIngredients(request):
    form = IngredientsForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def formRecipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def formBook(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def editBook(request, book_id):
    rec = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance = rec)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/edit.html', {'form': form})
    
def delBook(request, book_id):
    ing = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        ing.delete()
    return render(request, 'recipes/delete.html', {'book_id': ing})

def formAdvice(request):
    form = AdviceForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def editAdvice(request, advice_id):
    rec = get_object_or_404(Advice, pk=advice_id)
    form = AdviceForm(request.POST or None, request.FILES or None, instance = rec)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/edit.html', {'form': form})
    
def delAdvice(request, advice_id):
    ing = get_object_or_404(Advice, pk=advice_id)
    if request.method == "POST":
        ing.delete()
    return render(request, 'recipes/delete.html', {'book_id': ing})

def formWarning(request):
    form = WarningForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/form.html', {'form': form})

def editWarning(request, war_id):
    rec = get_object_or_404(BadThings, pk=war_id)
    form = WarningForm(request.POST or None, request.FILES or None, instance = rec)
    if form.is_valid():
        form.save()
    return render(request, 'recipes/edit.html', {'form': form})
    
def delWarning(request, war_id):
    ing = get_object_or_404(BadThings, pk=war_id)
    if request.method == "POST":
        ing.delete()
    return render(request, 'recipes/delete.html', {'war_id': war_id})
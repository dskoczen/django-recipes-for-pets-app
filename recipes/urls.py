from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<pk>/results/', views.ResultsView.as_view(), name='results'),
    path('comments/', views.comments, name='comments'),
    path('book/', views.book, name='book'),
    path('advice/', views.advice, name='advice'),
    path('warnings/', views.warnings, name='warnings'),
    path('recipes/comment', views.add_comment_to_recipe, name='add_comment_to_recipe'),
    path('formCat/', views.formCategory, name='formCategory'),
    path('delete/<category_id>', views.delCategory, name='delCategory'),
    path('edit/<category_id>', views.editCategory, name='editCategory'),
    path('formIng/', views.formIngredients, name='formIngredients'),
    path('formRec/', views.formRecipe, name='formRecipe'),
    path('formBook/', views.formBook, name='formBook'),
    path('delete/<book_id>', views.delBook, name='delBook'),
    path('book/edit/<book_id>', views.editBook, name='editBook'),
    path('formAdvice/', views.formAdvice, name='formAdvice'),
    path('delete/<advice_id>', views.delAdvice, name='delAdvice'),
    path('advice/edit/<advice_id>', views.editAdvice, name='editAdvice'),
    path('formWarning/', views.formWarning, name='formWarning'),
    path('warnings/delete/<war_id>', views.delWarning, name='delWarning'),
    path('warning/edit/<war_id>', views.editWarning, name='editWarning'),
]
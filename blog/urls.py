from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.listes_article, name='liste'),
    path('article/new/', views.ArticleCreate.as_view(), name="creer"),
    path('article/<int:id>/', views.article_details, name='details'),
    path('article/<int:id>/update', views.ArticleUpdate.as_view(), name="modifier"),
    path('article/<int:id>/delete', views.ArticleDelete.as_view(), name="supprimer"),
    path('article/brouillon', views.BrouillonList.as_view(), name="brouillon"),
]
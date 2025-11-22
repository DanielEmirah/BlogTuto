from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Article

def listes_article(request):
    articles = Article.objects.filter(publie=True).order_by("-date_creation")
    nbArticle = Article.objects.filter(publie=True).count()
    return render(request, "blog/liste.html", {"articles": articles,
                                               "nombres": nbArticle})

def article_details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "blog/details.html", {"article": article})

class BrouillonList(ListView):
    model = Article
    template_name = 'blog/brouillon.html'
    context_object_name = 'articles'  # Nom dans le template
    paginate_by = 10  # Pagination automatique
    
    def get_queryset(self):
        """Personnaliser la requête"""
        return Article.objects.filter(publie=False).order_by('-date_creation')

class ArticleCreate(CreateView):
    model = Article
    fields = ["titre", "contenu", "publie"]
    template_name = "blog/formulaire.html"
    success_url = reverse_lazy("blog:liste")

    def form_valid(self, form):
        """Mettre l'utilisateur comme auteur"""
        form.instance.auteur = self.request.user
        return super().form_valid(form)
    
class ArticleUpdate(UpdateView):
    model = Article
    fields = ["titre", "contenu", "publie"]
    pk_url_kwarg = "id" #Demande à django de récupérer l'id dans les urls.py au lieu de pk
    template_name = "blog/formulaire.html"
    success_url = reverse_lazy("blog:liste")

class ArticleDelete(DeleteView):
    model = Article
    pk_url_kwarg = "id" #Demande à django de récupérer l'id dans les urls.py au lieu de pk
    template_name = "blog/confirmer_suppression.html"
    success_url = reverse_lazy("blog:liste")
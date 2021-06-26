from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.db.models import Q, query

from .models import Book

class BookListView(LoginRequiredMixin,ListView):
    model=Book
    context_object_name='book_list'
    template_name='books/book_list.html'
    login_url='account_login'
    
class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=Book
    template_name='books/book_detail.html'
    login_url='account_login'
    permission_required = 'books.special_status'
    
class SearchResultListView(ListView):
    model=Book
    context_object_name='book_list'
    template_name='books/search_result.html'
    #queryset=Book.objects.filter(title__icontains='beginners')
    
    def get_queryset(self):
        query=self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
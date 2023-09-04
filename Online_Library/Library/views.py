from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .serializers import *


class HomePageView(TemplateView):
    template_name = 'base.html'


class BookListView(ListView):
    model = Books
    template_name = 'books_list.html'


class BookDetailView(DetailView):
    model = Books
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')


class MemberListView(ListView):
    model = Members
    template_name = 'member_list.html'


class MemberDetailView(DetailView):
    model = Members
    template_name = 'member_detail.html'


class MemberCreateView(CreateView):
    model = Members
    form_class = MemberForm
    template_name = 'member_form.html'
    success_url = reverse_lazy('member-list')


class MemberUpdateView(UpdateView):
    model = Members
    form_class = MemberForm
    template_name = 'member_form.html'
    success_url = reverse_lazy('member-list')


class BookBorrowingViewSet(viewsets.ModelViewSet):
    queryset = BookBorrowing.objects.all()
    serializer_class = BookBorrowingSerializer

    def create(self, request, *args, **kwargs):
        book_id = self.request.data.get('book')
        member_id = self.request.data.get('member')

        book = get_object_or_404(Books, pk=book_id)

        if book.available_copies > 0:
            borrowing = BookBorrowing.objects.create(book=book, member_id=member_id)
            book.available_copies -= 1
            book.save()
            serializer = self.get_serializer(borrowing)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "No available copies of the book."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book = instance.book
        book.available_copies += 1
        book.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

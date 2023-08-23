from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Books, Author, Members
from .serializers import BooksSerializer, AuthorSerializer, MembersSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class MembersViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        books_isbn = request.data.get('books', [])
        books_taken = []

        for isbn in books_isbn:
            try:
                book = Books.objects.get(isbn=isbn)
                if book.available_copies > 0:
                    book.available_copies -= 1
                    book.save()
                    books_taken.append(book)
            except Books.DoesNotExist:
                pass  # Ignore if the book doesn't exist

        if not books_taken:
            return Response({"detail": "No books available or provided."}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

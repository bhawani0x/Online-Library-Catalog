from rest_framework import serializers
from .models import BookBorrowing


class BookBorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookBorrowing
        fields = '__all__'

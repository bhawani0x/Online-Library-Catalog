from django.db import models


class Books(models.Model):
    isbn = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=120)  # Fixed typo: tittle -> title
    genre = models.CharField(max_length=120)
    publication = models.CharField(max_length=120)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ===> {self.isbn}"

    def take_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.save()


class Author(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    dob = models.DateField()
    nationality = models.CharField(max_length=120)
    books = models.ManyToManyField(Books, blank=True)

    def __str__(self):
        return f"{self.name} ==>> {self.nationality}"


class Members(models.Model):
    member_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    dob = models.DateField()
    doj = models.DateField()
    books = models.ManyToManyField(Books, blank=True)

    def __str__(self):
        return f"{self.name} ==>> {self.member_id}"

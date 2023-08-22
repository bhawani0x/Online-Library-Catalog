from django.db import models


class Books(models.Model):
    isbn = models.PositiveIntegerField(primary_key=True)
    tittle = models.CharField(max_length=120)
    genre = models.CharField(max_length=120)
    publication = models.CharField(max_length=120)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ===> {self.isbn}"


class Author(models.Model):
    author_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now_add=True)
    natioanlity = models.CharField(max_length=120)
    books = models.ManyToManyField(Books, blank=True, on_delete=models.Cascade)

    def __str__(self):
        return f"{self.name} ==>> {self.natioanlity}"


class Members(models.Model):
    member_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    dob = models.DateField(auto_now_add=True)
    doj = models.DateField(auto_now_add=True)
    books = models.ManyToManyField(Books, blank=True, on_delete=models.Cascade)

    def __str__(self):
        return f"{self.name} ==>> {self.member_id}"

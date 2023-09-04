from django.db import models


class Books(models.Model):
    isbn = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=120)  # Fixed typo: tittle -> title
    genre = models.CharField(max_length=120)
    publication = models.CharField(max_length=120)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ===> {self.isbn} ===> available_copies {self.available_copies}"



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

    def __str__(self):
        return f"{self.name} ==>> {self.member_id}"


class BookBorrowing(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Borrowed by {self.member.name}: {self.book.title}"
from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()  # Assuming you want a description field
    search_vector = SearchVectorField(null=True, blank=True)  # Field for full-text indexing

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'  # Ensure it matches your raw query table name

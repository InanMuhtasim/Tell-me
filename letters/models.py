import random
import string
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Confession(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='confessions')
    letter_receiver = models.CharField(max_length=20)
    letter_id = models.SlugField(max_length=50, primary_key=True)
    key= models.CharField(max_length=20)
    message = models.TextField()
    
    def generate_unique_letter_id(self):
        # Generate a random string of 10 letters
        random_letters = f"{self.creator.username}-" +''.join(random.choices(string.ascii_lowercase, k=10))
        # Ensure the letter_id is unique in the database
        while Confession.objects.filter(letter_id=random_letters).exists():
            random_letters = f"{self.creator.username}-" +''.join(random.choices(string.ascii_lowercase, k=10))
        return random_letters

    def save(self, *args, **kwargs):
        if not self.letter_id:
            self.letter_id = self.generate_unique_letter_id()
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "confession"
    
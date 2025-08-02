
from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name

class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    difficulty = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question[:30]}..."

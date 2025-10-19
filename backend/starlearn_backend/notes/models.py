from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    next_review = models.DateTimeField(null=True, blank=True)
    mastered = models.BooleanField(default=False)
    review_count = models.IntegerField(default=0)
    last_reviewed = models.DateTimeField(null=True, blank=True)
    interval_days = models.IntegerField(default=1)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'next_review']),
            models.Index(fields=['user', 'mastered']),
        ]

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def __repr__(self):
        return f"<Note: {self.title} - {self.user.username}>"
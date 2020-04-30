from django.db import models


class Memo(models.Model):
    title = models.CharField(max_length=150)        # default: blank=False, null=False
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
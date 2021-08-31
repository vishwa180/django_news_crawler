from django.db import models


class NewsArticle(models.Model):
    title = models.TextField(null=False, blank=False)
    url = models.TextField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "{}".format(self.title)

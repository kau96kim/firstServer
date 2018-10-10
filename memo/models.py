from django.db import models


class Memo(models.Model):
    content = models.CharField(max_length=1000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now_add=True)

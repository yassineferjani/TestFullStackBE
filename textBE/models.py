from django.db import models


class jsondoc(models.Model):
    document = models.TextField(null=False, default="")

    def __str__(self):
        return self.text

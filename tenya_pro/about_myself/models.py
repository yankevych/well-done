from django.db import models


class Myself(models.Model):
    about_myself_text = models.TextField('text')

    def __str__(self):
        return self.about_myself_text

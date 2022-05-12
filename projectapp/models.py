from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
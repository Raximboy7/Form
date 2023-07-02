from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    data = models.DateField()
    slug = models.SlugField()
        
    def __str__(self) -> str:
        return self.firstname + ' | ' + self.slug

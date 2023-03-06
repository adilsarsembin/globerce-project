from django.db import models

# Create your models here.


class Status:
    CREATED = 'CRE'
    UPDATED = 'UPD'
    DELETED = 'DEL'
    STATUS_CHOICES = [(CREATED, 'Created'),
                      (UPDATED, 'Updated'),
                      (DELETED, 'Deleted')]


class Header(models.Model):

    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

# не успел до статусов
# вторая задача вроде через tree
from django.db import models


# Create your models here.
class Entries(models.Model):
    """ This class represent a single database entry.
    """
    timestamp = models.DateTimeField()
    temperature = models.CharField(max_length=255, blank=False)
    duration = models.CharField(max_length=255, blank=False)
    
    class Meta:
        db_table = 'entries'

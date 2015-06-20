from django.db import models
from django.core.validators import URLValidator
from jsonfield import JSONField
# Create your models here.

class Stuend(models.Model):
    '''
    It stores information about the Students of college.
    '''


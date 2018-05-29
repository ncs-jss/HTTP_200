from django.db import models
from django.contrib.auth.models import User


class department(models.Model):
    '''
    Stores the detail of department linked with its newsletters
    '''
    department = models.CharField(max_length=50,
                                  blank=False,
                                  null=False)

    def __unicode__(self):
        return "%s" % (self.department)


class papers(models.Model):
    '''
    Stores the pdfs of newsletters
    '''
    name = models.CharField(null=False,
                            max_length=25)
    uploaded_by = models.ForeignKey(User)
    year = models.DateField()
    paper = models.FileField(upload_to="newsletters", blank=False, null=False)
    department = models.ForeignKey(department)

    def __unicode__(self):
        return "%s" % (self.name)

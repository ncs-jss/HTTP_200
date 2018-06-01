from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class department(models.Model):
    '''
    Stores the detail of department linked with its newsletters
    '''
    department = models.CharField(max_length=50,
                                  blank=False,
                                  null=False)

    def __unicode__(self):
        return "%s" % (self.department)


class newsletters(models.Model):
    '''
    Stores the pdfs of newsletters
    '''
    title = models.CharField(null=False,
                             max_length=25)
    uploaded_by = models.ForeignKey(User)
    year = models.DateField()
    paper = models.FileField(upload_to="newsletters",
                             blank=False,
                             null=False)
    department = models.ForeignKey(department)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    def create_newsletter(self):
        self.created_at = timezone.now()
        self.modified_at = timezone.now()

    def modify_newsletter(self):
        self.modified_at = timezone.now()

    def __unicode__(self):
        return "%s" % (self.title)

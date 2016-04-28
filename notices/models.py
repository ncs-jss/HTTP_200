from django.contrib.auth.models import User
from django.db import models
from profiles.models import FacultyDetail
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
import os

# Create your models here.


class Notice(models.Model):
    '''
    It stores the information about the Notices
    '''
    ACADEMICS = 'ACD'
    ADMINISTRATION = 'ADMN'
    TNP = 'TNP'
    EVENTS = 'EVNT'
    MISC = 'MISC'
    CATEGORY = (
        (ACADEMICS, 'Academics'),
        (ADMINISTRATION, 'Administration'),
        (TNP, 'Training and Placement'),
        (EVENTS, 'Events'),
        (MISC, 'Miscelleneous'),
    )
    faculty = models.ForeignKey(FacultyDetail)
    title = models.CharField(max_length=500)
    description = RichTextField()
    file_attached = models.FileField(upload_to="attachments", blank=True, null=True)
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=4,
                                choices=CATEGORY,
                                default=MISC)
    course_branch_year = models.CharField(max_length=200, blank=False, null=True)
    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)
    # scheduled_time = models.DateTimeField(blank=True,auto_now_add=True)

    def get_absolute_url(self):
        return reverse('notice_show', args=[self.pk])

    def filename(self):
        return os.path.basename(self.file.name)

    def is_bookmarked_by_user(self, request):
        # try:
        print request
        BookmarkedNotice.objets.get(notice__id=self.id, user=request.user)
        return "asdasdasdasd"
        # except:
        #     return False

    def __unicode__(self):
        return self.title


class BookmarkedNotice(models.Model):
    """
            Defines the databse table for storing the bookmarks as done by the user.
    """
    user = models.ForeignKey(User)
    notice = models.ForeignKey(Notice)
    pinned = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)


class TrendingInCollege(models.Model):
    title = models.CharField(max_length=200, blank=False)
    small_description = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField()
    visibility = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)

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
    ACADEMICS = 'academics'
    ADMINISTRATION = 'administration'
    TNP = 'tnp'
    EVENTS = 'events'
    MISC = 'misc'
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
    category = models.CharField(max_length=15,
                                choices=CATEGORY,
                                default=MISC)
    visible_for_student = models.BooleanField(default=True)
    visible_for_hod = models.BooleanField(default=False)
    visible_for_faculty = models.BooleanField(default=False)
    visible_for_management = models.BooleanField(default=False)
    visible_for_others = models.BooleanField(default=False)
    course_branch_year = models.CharField(max_length=200, blank=True, null=True, default="AllCourses-AllBranches-AllYears-AllSections")
    created = models.DateTimeField("Created", null=True, auto_now_add=True)
    modified = models.DateTimeField("Last Modified", null=True, auto_now=True)
    # scheduled_time = models.DateTimeField(blank=True,auto_now_add=True)

    def get_absolute_url(self):
        return reverse('notice_show', args=[self.pk])

    def filename(self):
        return os.path.basename(self.file.name)

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
    attachment = models.FileField(upload_to="trending", blank=True, null=True)
    visibility = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)

    def filename(self):
        return os.path.basename(self.file.name)

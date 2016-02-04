from django.test import TestCase
from .models import Notice,NoticeBranchYear,BookmarkedNotice
from profiles.models import FacultyDetail
from django.contrib.auth.models import User
# Create your tests here.

#models test
class NoticeTest(TestCase):
    
    def setUp(self):
        user=User.objects.create(username='Ajay',password='5678')
        faculty=FacultyDetail.objects.create(designation="teacher",department="IT",contact_no=9988213123,address="Indirapuram",alternate_email='abc@gmail.com',display_to_others='',user=user)
        Notice.objects.create(faculty=faculty,title='extra-class',description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow',file_attached='',subject='compiler design class',category='Academics')
        
    def test_create_notice(self):
        p=User.objects.get(username='Ajay')
        q=FacultyDetail.objects.get(user=p)
        details=Notice.objects.get(faculty=q)
        self.assertEquals(details.title,'extra-class')
        self.assertEquals(details.faculty.designation,'teacher')
        
class NoticeBranchYearTest(TestCase):
    
    def setUp(self):
        user=User.objects.create(username='Ajay',password='5678')
        faculty=FacultyDetail.objects.create(designation="teacher",department="IT",contact_no=9988213123,address="Indirapuram",alternate_email='abc@gmail.com',display_to_others='',user=user)
        notice=Notice.objects.create(faculty=faculty,title='extra-class',description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow',file_attached='',subject='compiler design class',category='Academics')
        NoticeBranchYear.objects.create(notice=notice)
        
    def test_create_noticebranchyear(self):
        p=User.objects.get(username='Ajay')
        q=FacultyDetail.objects.get(user=p)
        r=Notice.objects.get(faculty=q)
        details=NoticeBranchYear.objects.get(notice=r)
        self.assertEquals(details.year,'ALL')
    
class BookmarkedNoticeTest(TestCase):
    
    def setUp(self):
        user=User.objects.create(username='Ajay',password='5678')
        faculty=FacultyDetail.objects.create(designation="teacher",department="IT",contact_no=9988213123,address="Indirapuram",alternate_email='abc@gmail.com',display_to_others='',user=user)
        notice=Notice.objects.create(faculty=faculty,title='extra-class',description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow',file_attached='',subject='compiler design class',category='Academics')
        bookmark=BookmarkedNotice.objects.create(user=user,notice=notice,pinned=True)
        
    def test_create_bookmark(self):
        p=User.objects.get(username='Ajay')
        q=FacultyDetail.objects.get(user=p)
        r=Notice.objects.get(faculty=q)
        details=BookmarkedNotice.objects.get(user=p,notice=r)
        self.assertEquals(details.pinned,True)

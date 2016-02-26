from django.test import TestCase
from .models import Notice, NoticeBranchYear, BookmarkedNotice
from profiles.models import FacultyDetail
from django.contrib.auth.models import User
# Create your tests here.

# models test


class NoticeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Ajay', password='5678')
        self.faculty = FacultyDetail.objects.create(designation="teacher", department="IT", contact_no=9988213123,
                                                    address="Indirapuram", alternate_email='abc@gmail.com', display_to_others='', user=self.user)
        Notice.objects.create(faculty=self.faculty, title='extra-class', description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow',
                              file_attached='', subject='compiler design class', category='Academics')

    def test_create_notice(self):
        user = User.objects.get(username='Ajay')
        faculty_detail = FacultyDetail.objects.get(user=user)
        notice_details = Notice.objects.get(faculty=faculty_detail)
        self.assertEqual(notice_details.title, 'extra-class')
        self.assertEqual(notice_details.faculty.designation, 'teacher')


class NoticeBranchYearTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Ajay', password='5678')
        self.faculty_detail = FacultyDetail.objects.create(
            designation="teacher", department="IT", contact_no=9988213123, address="Indirapuram", alternate_email='abc@gmail.com', display_to_others='', user=self.user)
        self.notice = Notice.objects.create(faculty=self.faculty_detail, title='extra-class',
                                            description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow', file_attached='', subject='compiler design class', category='Academics')
        NoticeBranchYear.objects.create(notice=self.notice)

    def test_create_noticebranchyear(self):
        user = User.objects.get(username='Ajay')
        faculty_detail = FacultyDetail.objects.get(user=user)
        notice = Notice.objects.get(faculty=faculty_detail)
        notice_branchyear_details = NoticeBranchYear.objects.get(notice=notice)
        self.assertEqual(notice_branchyear_details.year, 'ALL')


class BookmarkedNoticeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Ajay', password='5678')
        self.faculty_detail = FacultyDetail.objects.create(
            designation="teacher", department="IT", contact_no=9988213123, address="Indirapuram", alternate_email='abc@gmail.com', display_to_others='', user=self.user)
        self.notice = Notice.objects.create(faculty=self.faculty_detail, title='extra-class',
                                            description='extra-class for compiler design will be from 1:30 to 2:30 tomorrow', file_attached='', subject='compiler design class', category='Academics')
        bookmark = BookmarkedNotice.objects.create(user=self.user, notice=self.notice, pinned=True)

    def test_create_bookmark(self):
        user = User.objects.get(username='Ajay')
        faculty_detail = FacultyDetail.objects.get(user=user)
        notice = Notice.objects.get(faculty=faculty_detail)
        bookmarked_notice = BookmarkedNotice.objects.get(user=user, notice=notice)
        self.assertEqual(bookmarked_notice.pinned, True)

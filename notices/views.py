from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from django.db.models import Q

from profiles.models import FacultyDetail, StudentDetail
from .models import Notice, BookmarkedNotice
from .forms import NoticeCreateForm

from datetime import datetime
from braces.views import LoginRequiredMixin, GroupRequiredMixin
import permissions


class NoticeList(LoginRequiredMixin, generic.View):

    def get(self, request):
        template = 'notices/list.html'
        print type(request.user)
        notice_list = Notice.objects.order_by('-modified')
        paginator = Paginator(notice_list, 10)
        page = request.GET.get('page')
        try:
            notices = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            notices = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            notices = paginator.page(paginator.num_pages)
        return render(request, template, {"notices": notices})


class NoticeShow(LoginRequiredMixin, generic.View):

    def get(self, request, pk=None):
        template_name = "notices/notice_detail.html"
        try:
            notice = Notice.objects.select_related('faculty').get(id=pk)
        except:
            return Http404()
        return render(request, template_name, {'notice': notice})


class CreateNotice(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    """
    View for creating the Notices
    """
    # model = Notice
    group_required = u'FacultyGroup'
    form_class = NoticeCreateForm
    exclude = ['faculty']
    success_url = '/notices'
    template_name = "notices/notice_form.html"
    # FIX THE BUG
    # raise_exception = True
    # redirect_unauthenticated_users = True

    def form_valid(self, form):
        faculty = get_object_or_404(FacultyDetail, user__id=self.request.user.id)
        branch_list = self.request.POST.getlist('branches')
        year_list = self.request.POST.getlist('semesters')
        course_list = self.request.POST.getlist('courses')
        form.instance.faculty = faculty
        form.instance.branches = " ".join(branch_list)
        form.instance.semesters = " ".join(year_list)
        form.instance.courses = " ".join(course_list)
        form.save()
        return super(CreateView, self).form_valid(form)


class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    form_class = NoticeCreateForm
    template_name = 'notices/notice_edit.html'
    success_url = reverse_lazy('notice_list')

    def get_queryset(self):
        base_queryset = super(NoticeUpdateView, self).get_queryset()
        notice = Notice.objects.get(id=self.kwargs['pk'])
        if self.request.user == notice.faculty.user:
            return base_queryset
        else:
            raise PermissionDenied()

    def form_valid(self, form):
        branch_list = self.request.POST.getlist('branches')
        semester_list = self.request.POST.getlist('semesters')
        course_list = self.request.POST.getlist('courses')
        form.instance.branches = " ".join(branch_list)
        form.instance.semesters = " ".join(semester_list)
        form.instance.courses = " ".join(course_list)
        return super(NoticeUpdateView, self).form_valid(form)


class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    success_url = reverse_lazy('notice_list')
    pass

    def delete(self, *args, **kwargs):
        return super(NoticeDeleteView, self).delete(self.get_object())


class BookmarkCreateView(LoginRequiredMixin, generic.View):
    '''
            Adding a Bookmark to a notice
    '''

    def post(self, request, pk=None):
        notice = Notice.objects.get(pk=pk)
        obj, created = BookmarkedNotice.objects.get_or_create(
            user=self.request.user,
            notice=notice)
        if created:
            return HttpResponse("Successfully Bookmarked")
        else:
            return HttpResponse("You have already bookmarked this notice")


class BookmarkListView(LoginRequiredMixin, generic.ListView):
    model = BookmarkedNotice
    """
	View for listing the bookmarked notices
	"""

    def get(self, request):
        template_name = "bookmark.html"
        bookmark_list = BookmarkedNotice.objects.filter(user=request.user).order_by('-pinned')
        paginator = Paginator(bookmark_list, 10)
        page = request.GET.get('page')
        try:
            bookmarks = paginator.page(page)
        except PageNotAnInteger:
            bookmarks = paginator.page(1)
        except EmptyPage:
            bookmarks = paginator.page(paginator.num_pages)
        return render(request, template_name, {"bookmarks": bookmarks})


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    '''
            Deleting a notice from Bookmark Notices List
    '''

    def post(self, request, pk=None):
        try:
            notice = get_object_or_404(Notice, pk=pk)
            BookmarkedNotice.objects.filter(user=self.request.user, notice=notice)[0].delete()
            return HttpResponse("Deleted the notice Successfully")
        except:
            return HttpResponse("Some error occured. Please try after sometime.")


class PinCreateView(LoginRequiredMixin, generic.View):

    def post(self, request, pk=None):
        try:
            '''
            only one pin is used for top so replacing the previous top pinned item to new one
            '''
            try:
                previous = BookmarkedNotice.objects.get(user=request.user, pinned=True)
                previous.pinned = False
                previous.save()
            except:
                pass

            bookmark = BookmarkedNotice.objects.get(pk=pk)
            bookmark.pinned = True
            bookmark.save()
            return HttpResponse("Pinned To Top")

        except:
            return HttpResponse("Some error occured.Please try after sometime")


class ReleventNoticeListView(LoginRequiredMixin, generic.View):

    def get(self, request):
        user = request.user
        template_name = "notices/list.html"
        try:
            faculty = get_object_or_404(FacultyDetail, user__id=self.request.user.id)
            notices = Notice.objects.filter(branches__contains=faculty.department)
        except:
            student = get_object_or_404(StudentDetail, user__id=self.request.user.id)
            notices = Notice.objects.filter(courses__contains=student.course, semesters__contains=student.semester, branches__contains=student.branch)
        return render(request, template_name, {'notices': notices})


class SearchNotices(LoginRequiredMixin, generic.View):

    def get(self, request):
        template = "notices/search.html"
        faculties = FacultyDetail.objects.all()
        Notices = Notice.objects.all()

        branches = request.GET.getlist('branches', '')
        for branch in branches:
            Notices = Notices.filter(branches__contains=branch)

        semesters = request.GET.getlist('semesters', '')
        for semester in semesters:
            Notices = Notices.filter(semesters__contains=semester)

        courses = request.GET.getlist('courses', '')
        for course in courses:
            Notices = Notices.filter(courses__contains=course)

        search_text = request.GET.get('search_text', '')
        uploaded_date = request.GET.get('uploaded_date', '')
        faculty = request.GET.get('faculty', '')

        try:
            Notices = Notices.filter(Q(faculty__contains=faculty) | Q(created__date=datetime.strptime(uploaded_date, "%d-%m-%Y").date()) | Q(description__contains=search_text) | Q(title__contains=search_text))
            Notices = Notices.order_by('-modified')
        except:
            pass

        paginator = Paginator(Notices, 10)
        page = request.GET.get('page')
        try:
            notices = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            notices = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            notices = paginator.page(paginator.num_pages)

        return render(request, template, {'faculties': faculties, 'notices': notices })

    
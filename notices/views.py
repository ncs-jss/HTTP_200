from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from django.core.exceptions import PermissionDenied
from notices.models import Notice, BookmarkedNotice, NoticeBranchYear
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import NoticeCreateForm
from profiles.models import FacultyDetail
import permissions
from django.views.generic import View

# Create your views here.


class NoticeList(LoginRequiredMixin, generic.View):

    def get(self, request):
        template = 'notices/list.html'
        print type(request.user)
        notice_list = Notice.objects.order_by('-updated_at')
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

# class NoticeDetail(LoginRequiredMixin, generic.View):
# DEPRECATED CODE
# 	def get(self, request, category = None):
# 		if category == "relevent":
# 			try:
# 				# if the logged in user is a student
# 				student = StudentDetail.objects.get(user__id = self.request.user.id)
# 				notices = NoticeBranchYear.objects.filter(year = student.year, branch = student.branch).values_list('notice', flat = True).order_by('-created_at')
# 				relevent_notices = Notice.objects.filter()
# 			except:
# 				# if the logged in user is a faculty
# 				faculty = FacultyDetail.objects.get(user__id = self.request.user.id)
# 		return


class NoticeCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
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
        form.instance.faculty = faculty
        form.save()
        branch_list = self.request.POST.getlist('branches')
        year_list = self.request.POST.getlist('years')
        for branch in branch_list:
            for year in year_list:
                print branch, year
                branchyear = NoticeBranchYear.objects.create(
                    notice=form.instance,
                    branch=branch,
                    year=year, )
        return super(NoticeCreateView, self).form_valid(form)

    # def get(self, request, *args, **kwargs):
    """
	View not in use
	"""
    # 	if not permissions.is_in_group(request.user, 'FacultyGroup'):
    # 		raise PermissionDenied()
    # 	else:
    # 		notice_form = NoticeCreateForm()
    # 		template_name = "notices/notice_form.html"
    # 		return render(request, template_name, {'form':notice_form})

    # def post(self, request):
    """
	View not in use
	"""
    # 	notice_form = NoticeCreateForm(request.POST)
    # 	faculty = get_object_or_404(FacultyDetail, user__id = self.request.user.id )
    # 	if notice_form.is_valid():
    # 		notice_obj = notice_form.save(commit=False)
    # 		notice_obj.faculty = faculty
    # 		notice_obj.save()
    # 	else:
    # 		return HttpResponse('Invalid Form')
    # 	return redirect("notice_list")


class NoticeUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    form_class = NoticeCreateForm
    template_name = 'notices/notice_edit.html'
    success_url = reverse_lazy('notice_list')

    def get_queryset(self):
        base_queryset = super(NoticeUpdateView, self).get_queryset()
        notice = Notice.objects.get(id=self.kwargs['pk'])
        # faculty = FacultyDetail.objects.get(user__id = self.request.user.id)
        if self.request.user == notice.faculty.user:
            return base_queryset
        else:
            raise PermissionDenied()

    def form_valid(self, form):
        NoticeBranchYear.objects.filter(
            notice=form.instance).delete()
        branch_list = self.request.POST.getlist('branches')
        year_list = self.request.POST.getlist('years')
        for branch in branch_list:
            for year in year_list:
                print branch, year
                branchyear = NoticeBranchYear.objects.create(
                    notice=form.instance,
                    branch=branch,
                    year=year, )
        return super(NoticeUpdateView, self).form_valid(form)


class NoticeDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    success_url = reverse_lazy('notice_list')
    pass

    def delete(self, *args, **kwargs):
        NoticeBranchYear.objects.filter(
            notice=self.get_object()).delete()
        return super(NoticeDeleteView, self).delete(self.get_object())


class BookmarkCreateView(LoginRequiredMixin, generic.View):
    '''
            Adding a Bookmark to a notice
    '''
    # def get(self, request, pk = None):
    # 	return HttpResponse("Get request working")

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
    '''
            Pinning Item to Top
    '''

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
                None

            bookmark = BookmarkedNotice.objects.get(pk=pk)
            bookmark.pinned = True
            bookmark.save()
            return HttpResponse("Pinned To Top")

        except:
            return HttpResponse("Some error occured.Please try after sometime")

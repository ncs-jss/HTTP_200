from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views import generic
from notices.models import Notice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import LoginRequiredMixin, GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import NoticeCreateForm
from profiles.models import FacultyDetail
import permissions

# Create your views here.
class NoticeList(LoginRequiredMixin, generic.View):
	def get(self, request):
		template = 'notices/list.html'
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
		return render_to_response(template, {"notices": notices})

class NoticeShow(LoginRequiredMixin, generic.View):
	def get(self, request, pk=None):
		template_name = "notices/notice_detail.html"
		try:
			notice = Notice.objects.select_related('faculty').get(id = pk)
		except:
			return Http404()
		return render(request, template_name, {'notice': notice})

class NoticeDetail(LoginRequiredMixin, generic.View):
	def get(self, request, category = None):
		if category == "relevent":
			try:
				# if the logged in user is a student
				student = StudentDetail.objects.get(user__id = self.request.user.id)
				notices = NoticeBranchYear.objects.filter(year = student.year, branch = student.branch).values_list('notice', flat = True).order_by('-created_at')
				relevent_notices = Notice.objects.filter()
			except:
				# if the logged in user is a faculty
				faculty = FacultyDetail.objects.get(user__id = self.request.user.id)

		return 

class NoticeCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
	# model = Notice
	group_required = u'FacultyGroup'
	form_class = NoticeCreateForm
	exclude = ['faculty']
	success_url = '/notices'
	template_name = "notices/notice_form.html"
	raise_exception = True
	# redirect_unauthenticated_users = True

	def form_valid(self, form):
		faculty = get_object_or_404(FacultyDetail, user__id = self.request.user.id )
		form.instance.faculty = faculty
		form.save()
		return super(NoticeCreateView, self).form_valid(form)

	# def get(self, request, *args, **kwargs):
	# 	if not permissions.is_in_group(request.user, 'FacultyGroup'):
	# 		raise PermissionDenied()
	# 	else:
	# 		notice_form = NoticeCreateForm()
	# 		template_name = "notices/notice_form.html"
	# 		return render(request, template_name, {'form':notice_form})

	# def post(self, request):
	# 	notice_form = NoticeCreateForm(request.POST)
	# 	faculty = get_object_or_404(FacultyDetail, user__id = self.request.user.id )
	# 	if notice_form.is_valid():
	# 		print "hah"
	# 		notice_obj = notice_form.save(commit=False)
	# 		notice_obj.faculty = faculty
	# 		notice_obj.save()
	# 	else:
	# 		return HttpResponse('Invalid Form')
	# 	return redirect("notice_list")

class NoticeUpdateView(LoginRequiredMixin,UpdateView):
	model = Notice
	success_url = reverse_lazy('server_list')


class NoticeDeleteView(LoginRequiredMixin,DeleteView):
	model = Notice
	success_url = reverse_lazy('server_list')
	pass

def my_custom_permission_denied_view(self, request):
	return render_to_response("kskks")
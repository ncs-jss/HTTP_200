from django.shortcuts import render, render_to_response
from django.views import generic
from notices.models import Notice
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from braces.views import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import NoticeCreateForm
from profiles.models import FacultyDetail

# Create your views here.
class NoticeList(LoginRequiredMixin, generic.View):
	def get(self, request):
		template = 'notices/list.html'
		notice_list = Notice.objects.order_by('-updated_at')
		paginator = Paginator(notice_list, 3)
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

class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeCreateForm
    success_url = '/notices'

    def form_valid(self, form):
    	faculty = FacultyDetail.objects.get(user__username = self.request.user.username)
    	form.instance.faculty = faculty
    	form.save()
        return super(NoticeCreateView, self).form_valid(form)

class NoticeUpdateView(LoginRequiredMixin,UpdateView):
	model = Notice
	success_url = reverse_lazy('server_list')
	pass

class NoticeDeleteView(LoginRequiredMixin,DeleteView):
	model = Notice
	success_url = reverse_lazy('server_list')
	pass
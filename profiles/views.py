from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from braces.views import LoginRequiredMixin
from django.views.generic import View
from .models import StudentDetail, FacultyDetail
from .forms import StudentForm, FacultyForm, UserForm
import permissions
from django.views.generic import TemplateView
from notices.models import Notice, TrendingInCollege


def bad_request_404(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response


def bad_request_500(request):
    response = render(request, '500.html')
    response.status_code = 500
    return response


class Home(View):
    '''
            Home Display view
    '''

    def get(self, request):
        template_name = 'index.html'
        trending = TrendingInCollege.objects.filter(visibility=True).order_by('-modified')
        notices = Notice.objects.all().order_by('-modified')[:5]
        return render(request, template_name, {'notices': notices, 'trending': trending})


class FaqDisplayView(TemplateView):
    '''
            FAQ Display Vieq
    '''
    template_name = 'faq.html'


class UserProfile(LoginRequiredMixin, View):
    '''
            To display the profiles of the Users
    '''

    def get(self, request, user_id=None):
        user_type = None
        user_list = get_object_or_404(User, username=user_id)
        detail_list = None
        if permissions.is_in_group(user_list, 'StudentGroup'):
            user_type = 'student'
            detail_list = get_object_or_404(StudentDetail, user=user_list)
        elif permissions.is_in_group(user_list, 'FacultyGroup'):
            user_type = 'faculty'
            detail_list = get_object_or_404(FacultyDetail, user=user_list)
        else:
            return Http404()

        template_name = 'profiles/profile.html'
        return render(request, template_name, {'user_type': user_type, 'user_list': user_list, 'detail_list': detail_list})

    def post(self, request, user_id=None):
        username = request.user
        detail = None

        if username == request.user:
            if permissions.is_in_group(username, 'StudentGroup'):
                user = get_object_or_404(User, pk=username.id)
                user_form = UserForm(request.POST, instance=user)
                detail = get_object_or_404(StudentDetail, user=user)
                detail_form = StudentForm(request.POST, instance=detail)

            elif permissions.is_in_group(username, 'FacultyGroup'):
                user = get_object_or_404(User, pk=username.id)
                user_form = UserForm(request.POST, instance=user)
                detail = get_object_or_404(FacultyDetail, user=user)
                detail_form = FacultyForm(request.POST, instance=detail)

            else:
                raise Http404("User Group not exist")

            if user_form.is_valid():
                user = user_form.save()

            if detail_form.is_valid():
                detail = detail_form.save()

            return redirect("user-profile", user_id=request.user.username)

        else:
            raise PermissionDenied

class EditProfile(LoginRequiredMixin, View):
    '''
    View for editing the profiles of the User
    '''

    def get(self, request, slug=None):
        username = request.user
        detail = None

        if permissions.is_in_group(username, 'StudentGroup'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(instance=user)
            detail = get_object_or_404(StudentDetail, pk=slug)
            detail_form = StudentForm(instance=detail)

        elif permissions.is_in_group(username, 'FacultyGroup'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(instance=user)
            detail = get_object_or_404(FacultyDetail, pk=slug)
            detail_form = FacultyForm(instance=detail)

        else:
            raise Http404("User Group not exist")

        template_name = "edit_profile.html"
        return render(request, template_name, {'userform': user_form, 'detailform': detail_form})

    def post(self, request, slug=None):
        username = request.user
        detail = None

        if permissions.is_in_group(username, 'StudentGroup'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(request.POST, instance=user)
            detail = get_object_or_404(StudentDetail, pk=slug)
            detail_form = StudentForm(request.POST, instance=detail)

        elif permissions.is_in_group(username, 'FacultyGroup'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(request.POST, instance=user)
            detail = get_object_or_404(FacultyDetail, pk=slug)
            detail_form = FacultyForm(request.POST, instance=detail)

        else:
            raise Http404("User Group not exist")

        if user_form.is_valid():
            user = user_form.save()

        if detail_form.is_valid():
            detail = detail_form.save()

        return redirect("user-profile", user_id=user.username)


def about(request, template_name='about.html'):
    return render(request, template_name,)


def contact(request, template_name='contact.html'):
    return render(request, template_name,)

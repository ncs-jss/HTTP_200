from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib import messages

from allauth.account.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from allauth.account.adapter import get_adapter
from allauth.account import signals
from braces.views import LoginRequiredMixin

from .models import StudentDetail, FacultyDetail, ContactMessage
from .forms import StudentForm, FacultyForm, UserForm
from notices.models import Notice, TrendingInCollege

from django.contrib.auth.models import Group
from notices.decorators import student_profile_complete, default_password_change
from django.utils.decorators import method_decorator


import permissions


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

    @method_decorator(default_password_change)
    @method_decorator(student_profile_complete)
    def get(self, request):
        template_name = 'index.html'
        trending = TrendingInCollege.objects.filter(visibility=True).order_by('-modified')

        if request.user.is_authenticated():
            user_group = request.user.groups.all()[0].name.lower()

            notices = Notice.objects.filter(**{'visible_for_'+user_group: True})
            notices = notices.order_by('-modified')[:5]
        else:
            notices = Notice.objects.filter(**{'visible_for_student': True})
            notices = notices.order_by('-modified')[:5]

        user_type = 'not_faculty'
        if request.user.is_authenticated and (permissions.is_in_group(request.user, 'faculty')):
            user_type = 'faculty'
        return render(request, template_name,
                      {'notices': notices, 'trending': trending, 'user_type': user_type})


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
        if permissions.is_in_group(user_list, 'student'):
            user_type = 'student'
            detail_list = get_object_or_404(StudentDetail, user=user_list)
        elif permissions.is_in_group(user_list, 'faculty'):
            user_type = 'faculty'
            detail_list = get_object_or_404(FacultyDetail, user=user_list)
        elif permissions.is_in_group(user_list, 'others'):
            user_type = 'others'
            detail_list = get_object_or_404(user_list)
        else:
            raise Http404()

        template_name = 'profiles/profile.html'
        return render(request, template_name, {'user_type': user_type, 'user_list': user_list, 'detail_list': detail_list})

    def post(self, request, user_id=None):
        username = request.user
        detail = None

        if username == request.user:
            if permissions.is_in_group(username, 'student'):
                user = get_object_or_404(User, pk=username.id)
                user_form = UserForm(request.POST, instance=user)
                detail = get_object_or_404(StudentDetail, user=user)
                detail_form = StudentForm(request.POST, instance=detail)

            elif permissions.is_in_group(username, 'faculty'):
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
                messages.success(self.request, 'Profile updated successfully.')
            else:
                messages.success(self.request, 'Error, Please enter correct details.')

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

        if permissions.is_in_group(username, 'student'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(instance=user)
            detail = get_object_or_404(StudentDetail, pk=slug)
            detail_form = StudentForm(instance=detail)

        elif permissions.is_in_group(username, 'faculty') or permissions.is_in_group(username, 'hod') or permissions.is_in_group(username, 'management') or permissions.is_in_group(username, 'others'):
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

        if permissions.is_in_group(username, 'student'):
            user = get_object_or_404(User, pk=username.id)
            user_form = UserForm(request.POST, instance=user)
            detail = get_object_or_404(StudentDetail, pk=slug)
            detail_form = StudentForm(request.POST, instance=detail)

        elif permissions.is_in_group(username, 'faculty'):
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


class Contact(View):
    def get(self, request):
        template_name = 'contact.html'
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contactus = ContactMessage(
            name=name,
            email=email,
            message=message)
        contactus.save()
        return redirect(reverse_lazy('contact'))


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    Custom class to override the password change view
    """
    success_url = reverse_lazy('home')

    # Override form valid view to keep user logged in
    def form_valid(self, form):
        form.save()
        # Update session to keep user logged in.
        update_session_auth_hash(self.request, form.user)

        get_adapter().add_message(self.request,
                                  messages.SUCCESS,
                                  'account/messages/password_changed.txt')
        signals.password_changed.send(sender=self.request.user.__class__,
                                      request=self.request,
                                      user=self.request.user)

        return super(PasswordChangeView, self).form_valid(form)

password_change = CustomPasswordChangeView.as_view()


def about(request, template_name='about.html'):
    return render(request, template_name,)


class BulkUser(LoginRequiredMixin, View):
    '''
    Custom class to create bulk student users.
    '''

    def get(self, request):
        username = request.user

        if username.is_superuser:
            return render(request, "bulkuserform.html")
        else:
            return render(request, "404.html")

    def post(self, request):
        user = request.user

        if user.is_superuser:
            admission_format = request.POST.get("admission_format")
            user_start = int(request.POST.get("start"))
            user_end = int(request.POST.get("end"))
            branch = request.POST.get("branch")
            year = request.POST.get("year")
            course = request.POST.get("course")
            group = str(request.POST.get("group"))
            group = Group.objects.get(name=group)

            if user_start < user_end:
                user_no = ["%.3d" % users for users in range(user_start, user_end+1)]
                for student in user_no:
                    profile = User.objects.filter(username=admission_format+str(student)).exists()
                    if profile:
                        pass
                    else:
                        new_user = User.objects.create_user(username=admission_format+str(student), password=str(admission_format)+str(student))
                        group.user_set.add(new_user)
                        StudentDetail.objects.create(user=new_user, branch=branch.upper(), year=year, course=course)
                return render(request, "bulkuser.html")
            else:
                return render(request, "bulkuserform.html", {"error": 1})
        else:
            return render(request, "404.html")


class SingleUser(LoginRequiredMixin, View):
    '''
    Custom Class to create single user.
    '''

    def get(self, request):
        user = request.user

        if user.is_superuser:
            return render(request, "singleuserform.html")
        else:
            return render(request, "404.html")

    def post(self, request):
        user = request.user

        if user.is_superuser:
            admission_format = request.POST.get("admission_format")
            branch = request.POST.get("branch")
            year = request.POST.get("year")
            course = request.POST.get("course")
            group = str(request.POST.get("group"))
            group = Group.objects.get(name=group)

            profile = User.objects.filter(username=admission_format).exists()
            if profile:
                pass
            else:
                new_user = User.objects.create_user(username=admission_format, password=admission_format)
                group.user_set.add(new_user)
                if (str(group) == "student"):
                    StudentDetail.objects.create(user=new_user, branch=branch, course=course, year=year)
                else:
                    FacultyDetail.objects.create(user=new_user)
            return render(request, "singleuser.html")
        else:
            return render(request, "404.html")

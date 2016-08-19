from django.contrib.auth.models import User
from profiles.models import StudentDetail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import check_password


def student_profile_complete(function):
    """
    Decorator to check that user profile is completed or not.
    """
    def wrapper(request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.user.username)
            profile = StudentDetail.objects.get(user=user)
        except:
            return function(request, *args, **kwargs)
        if user.first_name == "" or user.last_name == "" or user.email == "" or profile.course == "" or profile.branch == "" or profile.year == "" or profile.contact_no == "" or profile.address == "" or profile.mother_name == "" or profile.father_name == "":
            return HttpResponseRedirect(reverse("user-profile", kwargs={"user_id": str(request.user.username)}))
        else:
            return function(request, *args, **kwargs)
    return wrapper


def default_password_change(function):
    """
    Decorator to check if user password is changed or not.
    """
    def password(request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.user.username)
        except:
            return function(request, *args, **kwargs)

        if check_password(str(request.user.username), user.password):
            return HttpResponseRedirect(reverse("password_change"))
        else:
            return function(request, *args, **kwargs)
    return password

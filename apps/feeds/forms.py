from django import forms


class LoginForm(forms.Form):
    useranme = forms.CharField(label='Enter Username', max_length=100)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput())


class UploadNotice(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    attachment = forms.FileField()
    description = forms.CharField(widget=forms.Textarea)
    course = forms.CharField()
    semester = forms.CharField()
    branch = forms.CharField()
    batch = forms.CharField()
    schedule_post = forms.DateTimeField()

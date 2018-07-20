from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models, forms


def list_departments(request):
    '''
    This displays the list of departments.
    '''
    departments = [
        {"Computer Science and Engineering": "CSE"},
        {"Information Technology": "IT"},
        {"Electronics and Communication Engineering": "ECE"},
        {"Civil Engineering": "CE"},
        {"Mechanical Engineering": "ME"},
        {"Electrical and Electronics Engineering": "EEE"},
        {"Instrumentation and Control Engineering": "IC"},
        {"Electrical Engineering": "EE"},
    ]
    return render(request, 'newsletters/newsletter.html', {'departments': departments})


def list_papers(request, dept):
    '''
    This displays the list of Newsletters of selected department.
    '''
    department = models.department.objects.filter(department=dept)
    papers = models.papers.objects.filter(department=department)
    return render(request, 'newsletters/newsletter.html', {"papers": papers})


def show_letters(request, letter_no):
    '''
    This displays the selected newsletter.
    '''
    papers = models.papers.objects.get(id=int(letter_no))
    with open(str(papers.paper.path), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=newsletter.pdf'
        pdf.close()
        return response


def upload_newsletter(request):
    '''
    This enables groups (except students) to upload newsletter.
    '''
    if request.user.is_authenticated():
        if str(request.user.groups.all()[0].name) in ['faculty', 'hod', 'management', 'others']:
            if request.method == 'POST':
                form = forms.upload_letter_form(request.POST, request.FILES)
                if(form.is_valid()):
                    letter = form.save(commit=False)
                    department = models.department.objects.get(department=str(request.POST['department']))
                    letter.department = department
                    letter.uploaded_by = request.user
                    letter.save()
                    return HttpResponseRedirect('/newsletters/'+str(request.POST['department'])+'/')
                else:
                    errors = form.errors
                    return render(request, 'newsletters/upload_letter.html', {'errors': errors})
            else:
                return render(request, 'newsletters/upload_letter.html', {})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/accounts/login/')

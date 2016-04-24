from notices.models import Notice
from django import forms
from ckeditor.widgets import CKEditorWidget


class NoticeCreateForm(forms.ModelForm):
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    MT = 'MT'
    MCA = 'MCA'
    MBA = 'MBA'
    MTECH = 'MTECH'
    ALL = 'ALL'
    COURSES = (
        (MCA, 'MCA'),
        (MBA, 'MBA'),
        (MTECH, 'MTECH'),
        (ALL, 'ALL')
    )

    BRANCHES = (
        (CSE, 'CSE'),
        (IT, 'IT'),
        (EE, 'EE'),
        (ECE, 'ECE'),
        (EEE, 'EEE'),
        (CE, 'CE'),
        (IC, 'ICE'),
        (ME, 'ME'),
        (MT, 'MT'),
        (ALL, 'ALL')
    )

    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    SEMESTERS = (
        (FIRST, '1'),
        (SECOND, '2'),
        (THIRD, '3'),
        (FOURTH, '4'),
        (FIFTH, '5'),
        (SIXTH, '6'),
        (SEVENTH, '7'),
        (EIGHTH, '8'),
        (ALL, 'ALL')
    )
    branches = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=BRANCHES)
    semesters = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SEMESTERS)
    courses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=COURSES)

    class Meta:
        model = Notice
        exclude = ('faculty', 'course_branch_sem')
        widgets = {'description': CKEditorWidget, }

    def __init__(self, *args, **kwargs):
        try:
            notice_instance = Notice.objects.filter(
            title=kwargs['instance']).values()

            course_set = set()
            branch_set = set()
            sem_set = set()

            course_branch_sem = notice_instance[0]['course_branch_sem']
            course_branch_sem_list =  course_branch_sem.strip().split()

            for item in course_branch_sem_list:
                item = item.split('-')
                course, branch, sem = item[0], item[1], item[2]
                course_set.add(course)
                branch_set.add(branch)
                sem_set.add(sem)
            
            kwargs['initial'].update({'courses': list(course_set)})
            kwargs['initial'].update({'branches': list(branch_set)})
            kwargs['initial'].update({'semesters': list(sem_set)})
        
        except:
            pass
        super(NoticeCreateForm, self).__init__(*args, **kwargs)

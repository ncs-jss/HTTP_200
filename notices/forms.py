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
    SEVENTH  = 7
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
        exclude = ('faculty', 'courses', 'branches', 'semesters')
        widgets = {'description': CKEditorWidget, }

    def __init__(self, *args, **kwargs):
        # notice_instance = Notice.objects.filter(
        #     title=kwargs['instance'])
        # branchyear_instance = NoticeBranchYear.objects.filter(
        #     notice=notice_instance).values()
        # year = list(set((object['year'] for object in branchyear_instance)))
        # branch = list(set((object['branch'] for object in branchyear_instance)))
        # kwargs['initial'].update({'branches': branch})
        # kwargs['initial'].update({'years': year})
        super(NoticeCreateForm, self).__init__(*args, **kwargs)

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
	BRANCH = (
		(CSE, 'Computer Science and Engineering'),
		(IT, 'Information Technology'),
		(EE, 'Electrical Engineering'),
		(ECE, 'Electronics and Communication Engineering'),
		(EEE, 'Electrical and Electronics Engineering'),
		(CE, 'Civil Engineering'),
		(IC, 'Instrumentation and Control Engineering'),
		(ME, 'Mechanical Engineering'),
		(MT, 'Manufacturing Technology'),
		(MCA, 'Masters of Computer Applications'),
		(MBA, 'Master of Business Adminsitration  '),
		(MTECH, 'Masters of Technology'),
		(ALL, 'All branches and Courses')
		)
	FIRST = 1
	SECOND = 2
	THIRD = 3
	FOURTH = 4
	YEAR = (
		(FIRST, 'First Year'),
		(SECOND, 'Second Year'),
		(THIRD, 'Third Year'),
		(FOURTH, 'Fourth Year'),
		(ALL, 'For all')
		)
	branches = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=BRANCH)
	years = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=YEAR)
	class Meta:
		model = Notice
		exclude = ('faculty',)
		widgets = {'description': CKEditorWidget,}
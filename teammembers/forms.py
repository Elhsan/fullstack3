from django import forms

from .models import TeamMember

class TeamMemberModelForm(forms.ModelForm):
	#admin_status = forms.BooleanField(required=False, )
	class Meta:
		model = TeamMember
		fields = [
			'first_name',
			'last_name',
			'email',
			'phone',
			'admin_status'
		]

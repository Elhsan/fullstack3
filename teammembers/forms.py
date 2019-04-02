from django import forms

from .models import TeamMember

class TeamMemberModelForm(forms.ModelForm):
	class Meta:
		# 'delete not used '
		exclude = ('delete',)
		model = TeamMember
		fields = [
			'first_name',
			'last_name',
			'email',
			'phone',
			'admin_status'
		]

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import TeamMember
from .forms import TeamMemberModelForm
# Create your views here.

class TeamMemberEditView(View):
	"""
	View for editing
	If save button is pressed, saves edited teammember and redirects to list page
	Delete href on page that can redirect to a delete page
	"""
	template_name = "teammembers/teammember_edit.html"
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			# form with POST method and individual teammember
			form = TeamMemberModelForm(request.POST, instance=obj)
			if request.method == "POST":
				if 'save_button' in request.POST:
					# if save submit button pushed
					if form.is_valid():
						form.save()
					context['object'] = obj
					context['form'] = form
				if 'del_button' in request.POST:
					# if delete button pushed
					obj.delete()
					context['object'] = obj
				return redirect('/teammembers/')
		return render(request, self.template_name, context) 


class TeamMemberUpdateView(View):
	"""
	Original view for changing existing data for teammembers, could not delete
	"""
	template_name = "teammembers/teammember_update.html"
	def get_object(self):
		# GET object method
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			# form with POST method passed in and individual teammember
			form = TeamMemberModelForm(request.POST, instance=obj)
			if form.is_valid():
				# saves form
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context) 



class TeamMemberDeleteView(View):
	"""
	Original view for deleting, now done in edit view
	"""
	template_name = "teammembers/teammember_delete.html"
	def get_object(self):
		# GET object method
		id = self.kwargs.get('id')
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		# GET method
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		# POST method
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = obj
			# redirects to list page
			return redirect('/teammembers/')
		return render(request, self.template_name, context) 


class TeamMemberCreateView(View):
	template_name = "teammembers/teammember_add.html"
	def get(self, request, *args, **kwargs):
		#GET method
		# empty context for form
		form = TeamMemberModelForm()
		context = {"form": form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		#POST method
		# Model form with POST method
		form = TeamMemberModelForm(request.POST)
		if form.is_valid():
			form.save()
		#form = TeamMemberModelForm()
		if request.method == "POST":
			# redirects back to list page
			return redirect('../')
		context = {"form": form}
		return render(request, self.template_name, context)


class TeamMemberListView(View):
	"""
	View for printing all of the teammembers
	"""
	template_name = "teammembers/teammember_list.html"
	queryset = TeamMember.objects.all()
	"""
	def get_queryset(self):
		return self.queryset
	"""
	def get(self, request, *args, **kwargs):
		#queryset = self.get_queryset
		#print(queryset)
		#context = {'object_list': self.get_queryset()}

		# queryset of all teammembers is context
		queryset = TeamMember.objects.all()
		context = {'object_list': queryset}
		return render(request, self.template_name, context)

class TeamMemberView(View):
	"""
	View of individual teammember
	"""
	template_name = "teammembers/teammember_detail.html"
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)






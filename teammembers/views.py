from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import TeamMember
from .forms import TeamMemberModelForm
# Create your views here.

class TeamMemberEditView(View):
	template_name = "teammembers/teammember_edit.html"
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm(request.POST, instance=obj)
			if request.method == "POST":
				if form.is_valid():
					form.save()
				context['object'] = obj
				context['form'] = form
				return redirect('/teammembers/')
		return render(request, self.template_name, context) 



class TeamMemberDeleteView(View):
	template_name = "teammembers/teammember_delete.html"
	def get_object(self):
		id = self.kwargs.get('id')
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			context['object'] = obj
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			obj.delete()
			context['object'] = obj
			return redirect('/teammembers/')
		return render(request, self.template_name, context) 



class TeamMemberUpdateView(View):
	template_name = "teammembers/teammember_update.html"
	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
		return obj

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if obj is not None:
			form = TeamMemberModelForm(request.POST, instance=obj)
			if form.is_valid():
				form.save()
			context['object'] = obj
			context['form'] = form
		return render(request, self.template_name, context) 


class TeamMemberCreateView(View):
	template_name = "teammembers/teammember_add.html"
	def get(self, request, *args, **kwargs):
		form = TeamMemberModelForm()
		context = {"form": form}
		#print(self)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = TeamMemberModelForm(request.POST)
		if form.is_valid():
			form.save()
		#form = TeamMemberModelForm()
		if request.method == "POST":
			return redirect('../')
		context = {"form": form}
		return render(request, self.template_name, context)


class TeamMemberListView(View):
	template_name = "teammembers/teammember_list.html"
	queryset = TeamMember.objects.all()

	def get_queryset(self):
		return self.queryset
	def get(self, request, *args, **kwargs):
		#queryset = self.get_queryset
		#print(queryset)

		#context = {'object_list': self.get_queryset()}
		queryset = TeamMember.objects.all()
		context = {'object_list': queryset}
		return render(request, self.template_name, context)

class TeamMemberView(View):
	template_name = "teammembers/teammember_detail.html"
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(TeamMember, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)






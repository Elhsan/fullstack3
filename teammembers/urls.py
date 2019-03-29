from django.urls import path
from .views import (
	TeamMemberCreateView,
	TeamMemberListView,
	TeamMemberView,
	TeamMemberUpdateView,
	TeamMemberDeleteView,
	TeamMemberEditView
)

app_name = 'teammembers'

urlpatterns = [
	path('add/', TeamMemberCreateView.as_view(), name='teammembers-create'),
	path('', TeamMemberListView.as_view(), name='teammembers-list'),
	path('<int:id>/', TeamMemberView.as_view(), name='teammembers-detail'),
	path('<int:id>/update/', TeamMemberUpdateView.as_view(), name='teammembers-update'),
	path('<int:id>/edit/delete/', TeamMemberDeleteView.as_view(), name='teammembers-delete'),
	path('<int:id>/edit/', TeamMemberEditView.as_view(), name='teammembers-edit'),
]
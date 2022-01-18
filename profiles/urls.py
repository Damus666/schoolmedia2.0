from django.urls import path
from .views import (my_profile_view, invites_received_view, invite_profiles_list_view, ProfileListView, reject_invatation, send_invatation, remove_from_friends
,accept_invatation, reject_invatation, ProfileDetailView, ProfileSearchView)

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='all-profiles-view'),
    path('search/user', ProfileSearchView.as_view(), name='profile-search-view'),
    path('my-profile', my_profile_view, name='my-profile-view'),
    path('my-requests', invites_received_view, name='my-invites-view'),
    #path('to-request', invite_profiles_list_view, name='invite-profiles-view'),
    path('send-request', send_invatation, name='send-invite'),
    path('remove-friend', remove_from_friends, name='remove-friend'),
    path('my-requests/accept', accept_invatation, name='accept-invite'),
    path('my-requests/reject', reject_invatation, name='reject-invite'),
    path('<slug>', ProfileDetailView.as_view(), name='profile-detail-view'),
]
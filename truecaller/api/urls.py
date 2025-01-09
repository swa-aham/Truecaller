from django.urls import path
from .views import UserCreateView, ContactListView, ContactDetailView
from .views import SpamReportView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contacts/<int:pk>/report_spam/', SpamReportView.as_view(), name='report-spam'),
]
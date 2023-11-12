from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('edit_entry/<slug:event>/', views.EntryUpdateView.as_view(), name='edit_entry'),
    path('delete_entry/<slug:event>/', views.EntryDeleteView.as_view(), name='delete_entry'),
    path('<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
]
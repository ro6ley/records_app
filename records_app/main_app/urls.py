from django.urls import path

from .views import EntriesListView, EntryDetailsView

urlpatterns = [
    path('entries/', EntriesListView.as_view(), name='entries_list_view'),
    path('entries/<pk>', EntryDetailsView.as_view(), name='entry_details_view'),
]

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Entries


class EntriesListView(ListView):
    template_name = 'entries_list.html'
    model = Entries
    context_object_name = 'entries'
    paginate_by = 20


class EntryDetailsView(DetailView):
    template_name = 'entry_details.html'
    model = Entries

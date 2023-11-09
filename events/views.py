from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event
from .forms import EntryForm
 

class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        entries = event.entries.filter(approved=True).order_by('created_on')

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "entries": entries,
                "entered": False,
                "entry_form": EntryForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        entries = event.entries.filter(approved=True).order_by('created_on')

        entry_form = EntryForm(data=request.POST)

        if entry_form.is_valid():
            entry_form.instance.email = request.user.email
            entry = entry_form.save(commit=False)
            entry.event = event
            entry.save()

        else:
            entry_form = EntryForm()


        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "entries": entries,
                "entered": True,
                "entry_form": EntryForm()
            },
        )
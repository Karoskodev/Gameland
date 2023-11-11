from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Event, Entry
from .forms import EntryForm
from django.contrib import messages
 

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

        entry_exists = Entry.objects.filter(user=request.user, event=event).exists()

        if not entry_exists:

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
        else:
            return render(
                request,
                "event_detail.html",
                {
                    "event": event,
                    "entries": entries,
                    "entry_exists": True,
                },
            )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        entries = event.entries.filter(approved=True).order_by('created_on')

        if request.user.is_authenticated:
            # Check if the user already has an entry for the event
            entry_exists = Entry.objects.filter(user=request.user, event=event).exists()

            # If the user doesn't have an entry, process the form
            if not entry_exists:
                entry_form = EntryForm(data=request.POST)
                if entry_form.is_valid():
                    entry_form.instance.email = request.user.email
                    entry = entry_form.save(commit=False)
                    entry.event = event
                    entry.user = request.user
                    entry.save()

                    messages.success(request, 'Your entry was successfully submitted!')

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
        else:
            return render(
                request,
                "event_detail.html",
                {
                    "event": event,
                    "entries": entries,
                    "entry_exists": True,
                },
            )

class EntryUpdateView(View):
    template_name = 'edit_entry.html'

    def get(self, request):
        # Get the current user's entry
        entry = Entry.objects.get(user=request.user)

        # Populate the form with the current entry data
        form = EntryForm(instance=entry)

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Get the current user's entry
        entry = get_object_or_404(Entry, user=request.user)

        # Populate the form with the current entry data and the submitted data
        form = EntryForm(request.POST, instance=entry)

        if form.is_valid():
            form.save()
            # Redirect to a home page 
            return redirect('home')  

        return render(request, self.template_name, {'form': form})

class EntryDeleteView(View):
    template_name = 'delete_entry.html'

    def get_object(self):
        # Retrieve the entry based on the user and any additional conditions if needed
        return get_object_or_404(Entry, user=self.request.user)

    def get(self, request, *args, **kwargs):
        entry = self.get_object()
        return render(request, self.template_name, {'entry': entry})

    def post(self, request, *args, **kwargs):
        entry = self.get_object()

        entry.delete()

        messages.success(request, 'Your entry was successfully deleted!')
        
        return redirect('home')
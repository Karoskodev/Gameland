from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Event, Entry
from .forms import EntryForm
from django.contrib import messages
 
# View for displaying a list of events
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('date')
    template_name = 'index.html'
    paginate_by = 6

# View for displaying details and handling entries for a specific event
class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        entries = event.entries.filter(approved=True).order_by('created_on')

        entry_exists = Entry.objects.filter(user=request.user, event=event).exists()

        # Render the appropriate template based on whether the user has already entered
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
                    messages.error(request, 'Your entry was not valid, please try again!')

                    return redirect('home')
            else:
                messages.error(request, 'Your entry already exists!')

                return redirect('home')
        else:
            messages.error(request, 'To submit an entry,please log in or register!')
            return redirect('home')

# View for updating an existing entry
class EntryUpdateView(View):
    template_name = 'edit_entry.html'

    def get(self, request, event, *args, **kwargs):
        # Get the current user's entry
        entry = Entry.objects.get(user=request.user, event__slug=event)

        # Populate the form with the current entry data
        form = EntryForm(instance=entry)

        return render(request, self.template_name, {'form': form})

    def post(self, request, event, *args, **kwargs):
        # Get the current user's entry
        entry = get_object_or_404(Entry, user=request.user, event__slug=event)

        # Populate the form with the current entry data and the submitted data
        form = EntryForm(request.POST, instance=entry)

        if form.is_valid():
            form.save()

            messages.success(request, 'Your entry was successfully edited!')
            # Redirect to a home page 
            return redirect('home')  

        return render(request, self.template_name, {'form': form})

# View for deleting an existing entry
class EntryDeleteView(View):
    template_name = 'delete_entry.html'

    def get_object(self, *args, **kwargs):
        
        queryset = Entry.objects.filter(user=self.request.user, event__slug=self.kwargs['event'])
        entry = get_object_or_404(queryset, *args, **kwargs)
        return entry

    def get(self, request, *args, **kwargs):
        entry = self.get_object()
        return render(request, self.template_name, {'entry': entry})

    def post(self, request, *args, **kwargs):
        # Handle form submission for deleting an existing entry
        entry = self.get_object()

        entry.delete()

        messages.success(request, 'Your entry was successfully deleted!')
        
        return redirect('home')
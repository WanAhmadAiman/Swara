from django.shortcuts import render
from record.models import Entry

def entry_list(request):
    entries = Entry.objects.all().order_by('id')
    return render(request, 'entries/entry_list.html', {'entries':entries})

from django.shortcuts import render, redirect
from .models import Record
from .forms import RecordForm

def record_form(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_form')  # Redirect to the same page after submission
    else:
        form = RecordForm()

    records = Record.objects.all()  # Fetch all records for display
    return render(request, 'tracker/record_form.html', {'form': form, 'records': records})



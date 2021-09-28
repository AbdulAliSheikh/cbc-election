from django.shortcuts import render
from .forms import VoterForm


def index(request):
    form = VoterForm()

    if request.method == 'POST':
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'forms/index.html', context)


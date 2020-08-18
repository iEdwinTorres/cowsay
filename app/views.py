from django.shortcuts import render
import subprocess

from app.models import Cow
from app.forms import CowsayForm


def index_view(request):
    if request.method == "POST":
        form = CowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get("text")
            Cow.objects.create(text=text)
            cow_process = subprocess.run(
                f"cowsay '{text}'", capture_output=True, shell=True
            ).stdout.decode("utf-8")
            form = CowsayForm()
            return render(request, "index.html", {
                "form": form,
                "welcome": "What does the cow say?",
                "subprocess": cow_process
            })

    form = CowsayForm()
    return render(request, "index.html", {"form": form, "welcome": "What does the cow say?"})


def history_view(request):
    # Citation 1 in README.md
    cows = Cow.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {"cowsay": cows})

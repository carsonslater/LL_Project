from django.shortcuts import render, redirect
from MainApp.forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.all()

    context = {"T": topics}

    return render(request, "MainApp/topics.html", context)


def topic(request, topic_id):
    t = Topic.objects.get(id=topic_id)

    entries = Entry.objects.filter(topic=t).order_by("-date_added")

    context = {"topic": t, "entries": entries}

    return render(request, "MainApp/topic.html", context)


def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect("MainApp:topics")

    context = {"form": form}
    return render(request, "MainApp/new_topic.html", context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()

            return redirect("MainApp:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "MainApp/new_entry.html", context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST, instance=entry)

        if form.is_valid():
            form.save()

            return redirect("MainApp:topic", topic_id=topic.id)

    context = {"topic": topic, "form": form, "entry": entry}
    return render(request, "MainApp/edit_entry.html", context)

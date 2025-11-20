from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "MainApp/index.html")


def topics(request):
    topics = Topic.objects.all()

    context = {"T": topics}

    return render(request, "MainApp/topics.html", context)


def topic(request, topic_id):
    t = Topic.objects.get(id=topic_id)

    entries = Entry.objects.filter(topic=t).order_by["-date_added"]

    context = {"topic": t, "entries": entries}

    return render(request, "MainApp/")

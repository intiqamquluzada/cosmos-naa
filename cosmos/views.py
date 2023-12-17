from django.shortcuts import render
from cosmos.models import CosmoPerson


def index_view(request):
    cosmos = CosmoPerson.objects.order_by("-created_at")
    re_p = request.GET.get("person")
    if re_p:
        cosmos = cosmos.filter(name__icontains=re_p)
    context = {
        "cosmos": cosmos,
    }
    return render(request, "index.html", context)


def detail_view(request, id):
    person = CosmoPerson.objects.get(id=id)

    context = {
        "person": person
    }
    return render(request, "plane-detail.html", context)


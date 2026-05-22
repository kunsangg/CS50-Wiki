from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import NewPageForm
import markdown2
import random

from . import util

def random_page(request):

    entries = util.list_entries()

    title = random.choice(entries)

    return redirect(
        "entry",
        title=title
    )


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    content = util.get_entry(title)

    if content is None:
        return render(
            request,
            "encyclopedia/error.html",
            {
                "message": "Page not found."
            }
        )

    html_content = markdown2.markdown(content)


    return render(
        request,
        "encyclopedia/entry.html",
        {
            "title": title,
            "content": html_content
        }
    )
def search(request):

    query = request.GET.get("q")

    entries = util.list_entries()

    # Exact match
    if query in entries:
        return redirect("entry", title=query)

    results = []

    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)

    return render(
        request,
        "encyclopedia/search.html",
        {
            "entries": results,
            "query": query
        }
    )

def create_page(request):

    if request.method == "POST":

        form = NewPageForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if util.get_entry(title):
                return render(
                    request,
                    "encyclopedia/error.html",
                    {
                        "message": "Entry already exists."
                    }
                )

            util.save_entry(title, content)

            return redirect(
                "entry",
                title=title
            )

    return render(
        request,
        "encyclopedia/create.html",
        {
            "form": NewPageForm()
        }
    )
def edit_page(request, title):

    if request.method == "POST":

        content = request.POST["content"]

        util.save_entry(title, content)

        return redirect(
            "entry",
            title=title
        )

    content = util.get_entry(title)

    return render(
        request,
        "encyclopedia/edit.html",
        {
            "title": title,
            "content": content
        }
    )
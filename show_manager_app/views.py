from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from . models import Show

def index(request):
    return redirect('/shows')

def new_show(request):
    return render(request, 'new_show.html')

def create(request):
    errors = Show.objects.test_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/shows/new')
    else:
        new_show = Show.objects.create(
            title = request.POST["title"],
            release_date = request.POST["release_date"],
            description = request.POST["description"],
            network = request.POST["network"]
        )
        return redirect(f'/shows/{new_show.id}')

def show_info(request, id):
    context = {
        "info": Show.objects.get(id = id)
    }
    print(context)
    return render(request, 'show_info.html', context)
    
def all_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def edit_show(request, id):
    
    return render(request, 'edit_show.html', {
        "old_info": Show.objects.get(id = id)
    })

def update_show(request, id):
    updated_show = Show.objects.get(id = id)
    errors = Show.objects.test_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/shows/{updated_show.id}/edit')
    else:
        updated_show.title = request.POST["title"]
        updated_show.network = request.POST["network"]
        updated_show.release_date = request.POST["release_date"]
        updated_show.description = request.POST["description"]
        updated_show.save()
        return redirect(f'/shows/{updated_show.id}')

def delete_show(request, id):
    show_to_delete = Show.objects.get(id = id)
    show_to_delete.delete()
    return redirect('/shows')
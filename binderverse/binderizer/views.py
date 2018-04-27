from .utils import download_dataset
from .models import BinderSetup
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.shortcuts import render


def binderize(request):
    try:
        doi = request.GET['doi']
    except KeyError:
        return render(request, 'index.html')

    binder_setup = BinderSetup.objects.filter(doi=doi)

    if not binder_setup.exists():
        # grab the file_ids
        download_folder = download_dataset(doi)
        # create a binder setup instance
        binder_setup = BinderSetup.objects.create(doi=doi, version="???", folder=download_folder)

    else:
        binder_setup = binder_setup.first()

    # redirect to binder link
    return HttpResponseRedirect(binder_setup.get_binder_link())


def done(request):
    return HttpResponse("=)")
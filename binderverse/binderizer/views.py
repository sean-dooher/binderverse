from .utils import download_dataset
from .utils import getVersionNumber
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

    if not binder_setup.exists() or (binder_setup.first().version != getVersionNumber(doi)):
        # grab the file_ids
        version_number = getVersionNumber(doi)
        download_folder = download_dataset(doi)
        # create a binder setup instance
        binder_setup = BinderSetup.objects.create(doi=doi, version=version_number, folder=download_folder)

    else:
        binder_setup = binder_setup.first()

    # redirect to binder link
    return HttpResponseRedirect(binder_setup.get_binder_link())


def done(request):
    return HttpResponse("=)")

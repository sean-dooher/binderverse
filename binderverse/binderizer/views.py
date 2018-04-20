from .utils import download_file, get_files_from_doi
from .models import BinderSetup
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from django.shortcuts import render


def binderize(request):
    try:
        doi = request.GET['doi']
    except KeyError:
        return HttpResponse("Missing one or more of the required attributes: doi", status=400)

    binder_setup = BinderSetup.objects.filter(doi=doi)

    if not binder_setup.exists():
        # grab the file_ids
        file_ids = get_files_from_doi(doi)

        # download each file to the folder
        for id in file_ids:
            download_file(id, )

        # create a binder setup instance

    else:
        binder_setup = binder_setup.first()

    # redirect to binder link
    return HttpResponseRedirect(binder_setup)

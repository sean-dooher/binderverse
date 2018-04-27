import urllib.request
import json
import sys
import os
import hashlib
from django.conf import settings

def download_file(directory_name, name, fileId):
    """Save file identified by FILEID to DIRECTORY_NAME
    directory_name: string"""

    url = settings.DATAVERSE_SERVER + "/api/access/datafile/" + str(fileId)
    urllib.request.urlretrieve(url, os.path.join(directory_name, name))


def download_dataset(DOI):
    """Download files in a dataset to directory given as md5 hash of given DOI. DOI given in form of "doi:xxxxxxx"""

    directory_name = hashlib.md5(str.encode(DOI)).hexdigest()
    url = settings.DATAVERSE_SERVER + "/api/datasets/export?exporter=dataverse_json&persistentId=" + str(DOI)
    try:
        contents = urllib.request.urlopen(url).read()
        dataset = json.loads(contents)

        if os.path.exists(directory_name):
            os.rmdir(directory_name)
        os.makedirs(directory_name)

        for f in dataset["datasetVersion"]["files"]:
            download_file(directory_name, f['label'], f["dataFile"]["id"])

    except Exception as e:
        print(f"Error: {e}")

    return directory_name

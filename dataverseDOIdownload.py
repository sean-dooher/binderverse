import urllib.request
import json
import sys
import os
import hashlib

def download_file(directory_name, fileId):
    """Save file identified by FILEID to DIRECTORY_NAME
    directory_name: string"""

    url = "http://js-170-58.jetstream-cloud.org/api/access/datafile/" + str(fileId)
    urllib.request.urlretrieve(url, directory_name + "/" + str(fileId))

def download_dataset(DOI):
    """Download files in a dataset to directory given as md5 hash of given DOI. DOI given in form of "doi:xxxxxxx"""

    directory_name = hashlib.md5(str.encode(DOI)).hexdigest()
    if not os.path.exists(directory_name):
        url = "http://js-170-58.jetstream-cloud.org/api/datasets/export?exporter=dataverse_json&persistentId=" + str(DOI)
        try:
            contents = urllib.request.urlopen(url).read()
            dataset = json.loads(contents)
            os.makedirs(directory_name)
            for f in dataset["datasetVersion"]["files"]:
                download_file(directory_name, f["dataFile"]["id"])
        except:
            print("Error: Invalid DOI")

if __name__ == "__main__":
    download_dataset(sys.argv[1])

import urllib.request
import json
import sys

def download_file(fileId):
    url = "http://js-170-58.jetstream-cloud.org/api/access/datafile/" + str(fileId)
    urllib.request.urlretrieve(url, str(fileId))

def download_dataset(DOI):
    """Download files in a dataset to current directory given a DOI in form of "doi:xxxxxxx"""

    url = "http://js-170-58.jetstream-cloud.org/api/datasets/export?exporter=dataverse_json&persistentId=" + str(DOI)
    contents = urllib.request.urlopen(url).read()
    dataset = json.loads(contents)
    for f in dataset["datasetVersion"]["files"]:
        download_file(f["dataFile"]["id"])

if __name__ == "__main__":
    download_dataset(sys.argv[1])

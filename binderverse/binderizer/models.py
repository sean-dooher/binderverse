from django.db import models

# TODO: add version checking for redownload


class BinderSetup(models.Model):
    doi = models.CharField(max_length=50)
    folder = models.FilePathField()
    version = models.CharField(max_length=50)

    def get_binder_link(self):
        return '/done'


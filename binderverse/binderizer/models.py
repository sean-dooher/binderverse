from django.db import models


class BinderSetup(models.Model):
    doi = models.CharField(max_length=50)
    folder = models.FilePathField()

    def get_binder_link(self):
        pass


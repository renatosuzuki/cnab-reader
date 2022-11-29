from django.db import models


class UploadFile(models.Model):
    cnab_file = models.FileField(upload_to="uploads")

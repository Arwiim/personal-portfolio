from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Blog(models.Model):
    title = models.CharField( max_length=50)
    description = RichTextUploadingField('Contenido')
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    date = models.DateField()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'blogs'

    def __str__(self):
        return str(self.pk) + ' - ' + self.title
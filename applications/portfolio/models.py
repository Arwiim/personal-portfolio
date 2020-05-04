from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=250)
    image = models.ImageField(upload_to='portfolio/')
    url = models.URLField(blank=True, null=True)
    date = models.DateField()

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Projects'
        db_table = 'projects'

    def __str__(self):
        return str(self.pk) + ' - ' + self.title
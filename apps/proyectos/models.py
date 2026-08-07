from django.db import models
from apps.proyectos.choices import ProjectStatus,MediaType

class Technology(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    icon = models.ImageField(
        upload_to='technologies/'
    )
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        max_length=255
        )
    short_description = models.TextField()
    description = models.TextField()
    technologies = models.ManyToManyField(
        Technology,
        related_name='Projects'
    )
    repository_url = models.URLField()
    live_url = models.URLField(
        blank=True,
        null=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        verbose_name='Estado del proyecto'
    )
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProjectMedia(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="media"
    )

    file = models.FileField(
        upload_to="projects/"
    )

    media_type = models.CharField(
        max_length=10,
        choices=MediaType.choices
    )

    order = models.PositiveIntegerField(
        default=0
    )
    
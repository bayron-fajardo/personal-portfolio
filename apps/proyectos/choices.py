from django.db import models

class ProjectStatus(models.TextChoices):
    development = 'development', 'En desarrollo'
    completed = 'completed', 'Completado'
    archived = 'archived', 'Archivado'
    
class MediaType(models.TextChoices):
    IMAGE = 'image', 'Imagen'
    VIDEO = 'video', 'Video'
from django.contrib import admin
from apps.proyectos.models import Project, Technology, ProjectMedia
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'status',
        'featured',
        'created_at',
    )
    
    list_filter = (
        'status',
        'featured',
    )
    
    search_fields = (
        'name',
        'description',
    )
    
    prepopulated_fields = {
        "slug": ("name",)
    }
    
    ordering = ("-created_at",)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'icon',
    )
    
    list_filter = (
        'name',
        'icon',
    )
    
    search_fields = (
        'name',
        'icon',
    )
    
@admin.register(ProjectMedia)
class ProjectMediaAdmin(admin.ModelAdmin):
    
    list_display = (
        'project',
        'file',
        'media_type',
        'order',
    )
    
    list_filter = (
        'project',
        'file',
        'media_type',
    )
    
    search_fields = (
        'project',
        'file',
    )
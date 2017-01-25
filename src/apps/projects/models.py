from django.db import models
from django_extensions.db.models import TitleDescriptionModel


class Project(TitleDescriptionModel):
    """Project model"""
    pass


class Task(TitleDescriptionModel):
    """Task model

    Attributes:
        project (Project): project of card

    """
    project = models.ForeignKey('Project')

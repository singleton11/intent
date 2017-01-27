from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class Project(TitleDescriptionModel, TimeStampedModel):
    """Project model"""
    pass


class Task(TitleDescriptionModel, TimeStampedModel):
    """Task model

    Attributes:
        project (Project): project of card
        completed (bool): completed flag
        completed_datetime (datetime): time when task was completed

    """
    project = models.ForeignKey('Project')
    completed = models.BooleanField()
    completed_datetime = models.DateTimeField(blank=True, null=True)

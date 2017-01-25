from django.apps.config import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProjectsAppConfig(AppConfig):
    """App config for merchants"""

    name = 'apps.projects'
    verbose_name = _('Projects')

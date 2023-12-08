from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "coverage_repro.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import coverage_repro.users.signals  # noqa: F401
        except ImportError:
            pass

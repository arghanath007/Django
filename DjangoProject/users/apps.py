from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # Django now knows about the signals in the signals.py file.
    def ready(self) -> None:
        import users.signals

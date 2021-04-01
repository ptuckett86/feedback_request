from django.core.mail import send_mail
from django.conf import settings


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "{0}/{1}".format(instance.pk, filename)


def send_urgent_mail(instance):
    if instance.is_urgent:
        send_mail(
            "URGENT FEEDBACK " + instance.subject,
            instance.body,
            settings.DEFAULT_FROM_EMAIL,
            settings.FEEDBACK_TO_EMAIL,
        )
    return instance

from uuid import uuid4
from django.db import models
from django.conf import settings
from feedback_app.methods import user_directory_path
from vote.models import VoteModel
from .fields import STATUS


class MetaModel(models.Model):
    """
    Provides information common to most every object in the database.
    """

    uuid = models.UUIDField(
        default=uuid4, editable=False, db_index=True, unique=True, primary_key=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class Feedback(VoteModel, MetaModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=60)
    body = models.TextField()
    status = models.CharField(max_length=60, choices=STATUS, default="submitted")
    attachment = models.ImageField(upload_to=user_directory_path, null=True)
    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class FeedbackResponse(MetaModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback = models.ForeignKey(
        Feedback, related_name="responses", on_delete=models.CASCADE
    )
    response = models.TextField()
    is_company = models.BooleanField(default=False)

    def __str__(self):
        return self.feedback

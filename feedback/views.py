from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from feedback_app.permissions import IsSuperUser
from .filters import FeedbackFilter, FeedbackResponseFilter
from .models import Feedback, FeedbackResponse
from .serializers import (
    FeedbackListSerializer,
    FeedbackResponseSerializer,
    FeedbackSerializer,
    FeedbackSuperUserSerializer,
)


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    Feedback for the app. User must be authenticated.

    ###Expandable fields:
        * owner
        
    """

    ordering_fields = (
        "created_at",
        "num_vote_up",
        "num_vote_down",
        "vote_score",
        "response_count",
    )
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filter_class = FeedbackFilter
    search_fields = ("owner__email", "subject", "body", "status")

    def get_queryset(self):
        return Feedback.objects.annotate(response_count=Count("responses"))

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return FeedbackSuperUserSerializer
        elif not self.request.user.is_superuser:
            return FeedbackSerializer
        elif self.action == "list":
            return FeedbackListSerializer
        return FeedbackListSerializer

    def get_permissions(self):
        return (IsAuthenticated(),)

    @action(methods=["get"], detail=True)
    def up_vote(self, request, pk=None):
        feedback = self.get_object()
        if feedback.votes.up(request.user) == False:
            return Response(
                {"status": "You've already up-voted"}, status=status.HTTP_200_OK
            )
        else:
            feedback.votes.up(request.user)
            return Response({"status": "Up-vote Saved"}, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True)
    def down_vote(self, request, pk=None):
        feedback = self.get_object()
        if feedback.votes.down(request.user) == False:
            return Response(
                {"status": "You've already down-voted"}, status=status.HTTP_200_OK
            )
        else:
            feedback.votes.down(request.user)
            return Response({"status": "Down-vote saved"}, status=status.HTTP_200_OK)


class FeedbackResponseViewSet(viewsets.ModelViewSet):
    """
    Feedback response. User must be signed in as a private profile. 

    ###Expandable fields:
        * owner
        * feedback

    """

    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_class = FeedbackResponseFilter
    search_fields = (
        "owner__email",
        "feedback__subject",
        "feedback__body",
        "feedback__status",
        "response",
    )

    def get_queryset(self):
        return FeedbackResponse.objects.all()

    def get_serializer_class(self):
        return FeedbackResponseSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

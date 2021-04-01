from django.db import transaction
from django.conf import settings
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from feedback_app.methods import send_urgent_mail
from .models import Feedback, FeedbackResponse


class FeedbackResponseSerializer(FlexFieldsModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="feedback_response-detail")

    class Meta:
        model = FeedbackResponse
        fields = [
            "url",
            "uuid",
            "created_at",
            "updated_at",
            "feedback",
            "owner",
            "response",
            "is_company",
        ]
        read_only_fields = ["owner", "is_company"]

    def create(self, validated_data):
        owner = self.context["request"].user
        feedback_response = FeedbackResponse.objects.create(
            **validated_data, owner=owner
        )
        if owner.is_superuser:
            feedback_response.is_company = True
            feedback_response.save()
        return feedback_response

    expandable_fields = {
        "owner": (settings.USER_SERIALIZER, {"source": "owner"}),
        "feedback": ("feedback.FeedbackListSerializer", {"source": "feedback"}),
    }


class FeedbackListSerializer(FlexFieldsModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="feedback-detail")
    responses = FeedbackResponseSerializer(read_only=True, many=True)
    response_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "url",
            "uuid",
            "created_at",
            "updated_at",
            "subject",
            "body",
            "status",
            "is_urgent",
            "vote_score",
            "num_vote_up",
            "num_vote_down",
            "owner",
            "attachment",
            "responses",
            "response_count",
        ]
        read_only_fields = [
            "owner",
            "status",
            "vote_score",
            "num_vote_up",
            "num_vote_down",
        ]

    expandable_fields = {
        "owner": (settings.USER_SERIALIZER, {"source": "owner"}),
        "responses": (
            "feedback.FeedbackResponseSerializer",
            {"source": "responses", "many": True},
        ),
    }


class FeedbackSuperUserSerializer(FeedbackListSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="feedback-detail")

    class Meta:
        model = Feedback
        fields = FeedbackListSerializer.Meta.fields
        read_only_fields = ["owner", "vote_score", "num_vote_up", "num_vote_down"]

    @transaction.atomic()
    def create(self, validated_data):
        owner = self.context["request"].user
        feedback = Feedback.objects.create(**validated_data, owner=owner)
        feedback.save()
        return feedback

    expandable_fields = FeedbackListSerializer.expandable_fields


class FeedbackSerializer(FeedbackListSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="feedback-detail")

    class Meta:
        model = Feedback
        fields = FeedbackListSerializer.Meta.fields
        read_only_fields = FeedbackListSerializer.Meta.read_only_fields

    @transaction.atomic()
    def create(self, validated_data):
        owner = self.context["request"].user
        feedback = Feedback.objects.create(**validated_data, owner=owner)
        feedback.save()
        send_urgent_mail(feedback)
        return feedback

    expandable_fields = FeedbackListSerializer.expandable_fields

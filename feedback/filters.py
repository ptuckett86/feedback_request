import django_filters
from .models import Feedback, FeedbackResponse
from .fields import STATUS


class FeedbackFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=STATUS)

    class Meta:
        model = Feedback
        fields = {
            "owner_id": ["exact"],
            "subject": ["icontains"],
            "body": ["icontains"],
            "status": ["exact"],
            "is_urgent": ["exact"],
        }


class FeedbackResponseFilter(django_filters.FilterSet):
    class Meta:
        model = FeedbackResponse
        fields = {
            "owner_id": ["exact"],
            "feedback_id": ["exact"],
            "response": ["icontains"],
        }


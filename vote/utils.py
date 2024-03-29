# from functools import wraps
from django.contrib.contenttypes.models import ContentType

# def instance_required(func):
#     @wraps(func)
#     def inner(self, *args, **kwargs):
#         if self.instance is None:
#             error = "Can't call %s with a non-instance manager" % func.__name__
#             raise TypeError(error)

#         return func(self, *args, **kwargs)

#     return inner


def add_field_to_objects(model, objects, user_id):
    from .models import Vote, UP, DOWN

    content_type = ContentType.objects.get_for_model(model)
    object_ids = [r.id for r in objects]

    voted_object_ids = Vote.objects.filter(
        user_id=user_id, content_type=content_type, object_id__in=object_ids
    ).values_list("object_id", "action")

    for r in objects:
        r.is_voted_up = (r.pk, UP) in voted_object_ids
        r.is_voted_down = (r.pk, DOWN) in voted_object_ids

    return objects

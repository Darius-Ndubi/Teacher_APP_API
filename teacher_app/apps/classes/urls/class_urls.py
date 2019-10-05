from django.urls import path
from ..views.classviews import (
    CreateClassView,
    ViewClasses
)

urlpatterns = [
    path('create/', CreateClassView.as_view(), name="add_new_class"),
    path('my_classes/', ViewClasses.as_view(), name="list_my_classes"),
]
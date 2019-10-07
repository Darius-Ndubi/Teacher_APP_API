from django.urls import path


from teacher_app.apps.classes.views.classviews import (
    CreateClassView,
    ViewClasses,
    EditClasses
)

urlpatterns = [
    path('create/', CreateClassView.as_view(), name="add_new_class"),
    path('my_classes/', ViewClasses.as_view(), name="list_my_classes"),
    path('<str:classname>/edit',
         EditClasses.as_view(), name="edit_my_class_name"),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', MessagesList.as_view()),
    path('register/', RegisterView.as_view()),
    path('task/create/', TaskCreateView.as_view()),
    path('task/list/', TaskListView.as_view()),
    path('task/update/<int:pk>', TaskUpdateView.as_view()),
    path('category/list', CategoryListView.as_view()),
    path('subcategory/list', SubcategoryListView.as_view()),
    path('category/create', CategoryCreateView.as_view()),
    path('subcategory/create', SubcategoryCreateView.as_view()),
    path('course/list/', CourseListView.as_view()),
    path('course/create/', CourseCreateView.as_view()),
    path('course/update/<int:pk>', CourseUpdateView.as_view()),
    path('tests/list', TestListView.as_view()),
    path('tests/create', TestCreateView.as_view()),
    path('tests/update/<int:pk>', TestUpdateView.as_view()),
    path('solution/create', SolutionView.as_view())
]

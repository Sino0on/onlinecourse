from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class MessagesList(generics.ListAPIView):
    serializer_class = MessageSerializer
    # queryset = Messages.objects.all()
    def get_queryset(self):
        user_id = self.request.user
        if user_id:
            ids = user_id.id
            return Messages.objects.filter(user=user_id)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = TaskCreateSerializer


class TaskListView(generics.ListAPIView):
    queryset = Tasks.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = TaskListSerializer


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Tasks.objects.all()


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer


class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategories.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = SubcategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = CategoryCreateSerializer


class SubcategoryCreateView(generics.CreateAPIView):
    queryset = Subcategories.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = SubcategoryCreateSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CourseListSerializer


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = CourseCreateSerializer


class CourseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    permission_classes = (IsAdminUser, )
    serializer_class = CourseCreateSerializer


class TheoryUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TheoryCreateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Theory.objects.all()


class TheoryListView(generics.RetrieveUpdateAPIView):
    serializer_class = TheoryListSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Theory.objects.all()


class TheoryCreateView(generics.RetrieveUpdateAPIView):
    serializer_class = TheoryCreateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Theory.objects.all()


class TestListView(generics.ListAPIView):
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Tests.objects.all()


class TestCreateView(generics.CreateAPIView):
    serializer_class = TestCreateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Tests.objects.all()


class TestUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = TestCreateSerializer
    permission_classes = (IsAdminUser, )
    queryset = Tests.objects.all()


class SolutionView(generics.CreateAPIView):
    serializer_class = SolutionCreateSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Solutions.objects.all()

    def post(self, request, *args, **kwargs):
        if request.data:
            a = dict(request.data)
            eval(a['solution'])
            tests = Tests.objects.filter(tasks=int(a['task']))
            for i in tests:
                print(i.test)
        return self.create(request, a)

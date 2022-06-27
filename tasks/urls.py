from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('taskitems/', views.TaskItemList.as_view()),
    path('taskitems/<int:pk>/', views.TaskItemDetail.as_view())
]

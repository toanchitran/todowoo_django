"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signUpUser, name="signupuser"),
    path('signin/', views.signInUser, name="signinuser"),
    path('signout/', views.signOutUser, name="signoutuser"),

    #Todos
    path('', views.home, name="home"),
    path('current_task/', views.currentTask, name="currenttodos"),
    path('create_task/', views.createTask, name="createtodos"),
    path('completed_tasks/', views.completedTasks, name="completedtodos"),
    path('todo/<int:todos_pk>', views.viewTask, name="viewtodo"),
    path('todo/<int:todos_pk>/complete',views.completeTask, name="completetodo"),
    path('todo/<int:todos_pk>/delete', views.deleteTask, name="deletetodo"),
]

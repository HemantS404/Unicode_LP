from django.urls import path
import ToDoList.views as views
 
urlpatterns = [
    path('', views.login_user, name='login'),
    path('index', views.index, name = 'index'),
    path('details/<int:id>', views.details, name = 'details'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('create', views.create, name = 'create'),
    path('update/<int:id>', views.update, name = 'update'),
    path('signup/', views.signup_user, name='signup'),
    path('logout/', views.logout_user, name='logout')
]
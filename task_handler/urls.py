from django.urls import path
import task_handler.views as views

urlpatterns = [
    path('', views.mainpage, name = 'mainpage'),
    path('details/<int:id>', views.details, name = 'details'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('create/', views.create, name = 'create'),
    path('update/<int:id>', views.update, name = 'update'),
]
from django.contrib import admin
from django.urls import path
from dare import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/<int:s>', views.student),
    path('stu/', views.student_details),

]

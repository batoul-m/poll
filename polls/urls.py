from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('time/', views.current_datetime),
]
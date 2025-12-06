from django.urls import include, path

handler404 = 'myapp.views.my_custom_page_not_found_view'
handler500 = 'myapp.views.my_custom_error_view'

urlpatterns = [
    path('author-polls/', include('polls.urls', namespace='author-polls')),
    path('publisher-polls/', include('polls.urls', namespace='publisher-polls')),
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('about/', MyView.as_view(greeting="Hello!"))
]
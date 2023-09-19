from django.urls import path
from .views import StudentView, GroupView
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', GroupView.as_view(), name='group'),
    path('student/', StudentView.as_view(), name='student'),
    path('group/<int:group_id>/', views.students_in_group, name='students_in_group'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
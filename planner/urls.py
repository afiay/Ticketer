from django.conf import settings
from . import views
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list'),
    path('<slug:slug>/', views.EventDetailView.as_view(), name='event-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
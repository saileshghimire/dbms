from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.base, name='home'),
    path("addstudent", views.addstudentinformation, name='addstudent'),
    path("search/", views.searchstudent, name="search"),
    path('views/',views.viewdata, name="view"),
    path('delete/', views.deletestudent , name="delete"),
    path('update/<int:id>', views.updatestudent, name="update"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

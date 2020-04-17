from django.urls import path
from . import views
from .views import delete
app_name = "news"


urlpatterns = [
    path('blog/', views.xemlist, name="trang chu"),
    path('blog/<int:id>/', views.urlport),
    path('blog/add', views.add_post, name="add"),
    path('blog/save', views.save_news, name="save"),
    path('blog/<int:id>/delete/', delete, name="xoa"),
]

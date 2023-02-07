from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_view, name = 'wall'),
    path('upload/', views.upload_view, name = 'upload_image'),
    path('like/<int:image_id>', views.like_request, name = 'like'),
    path('unlike/<int:image_id>', views.unlike_request, name = 'unlike'),
    path('send_mail', views.send_me_a_message, name="message")
]
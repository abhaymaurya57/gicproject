from django.urls import path
from . import views

urlpatterns = [
    path('',views.gic2,name="gic2"),
    # path('gallery/',views.gallery,name="gallery"),
    # path('gallery/<int:image_id>/', views.image_detail, name='image_detail'),

    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('contact/', views.contact, name='contact'),
]
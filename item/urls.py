from django.contrib import admin
from django.urls import path

from . import views
app_name = 'item'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/<int:pk>/', views.detail, name='detail'),
 ]

# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import item_detail, item_list  # Assuming you have views for listing and details

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', item_list, name='item_list'),  # Adjust based on your actual view names
#     path('item/<int:item_id>/', item_detail, name='item_detail'),  # Detail view for each item
# ]

# if settings.DEBUG:  # Serve media files during development
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
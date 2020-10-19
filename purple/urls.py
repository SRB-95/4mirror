from .import views					
from django.urls import path
				
app_name = 'purple'                
urlpatterns = [
    path('', views.index,name="index"),
    path('<int:item_id>/', views.detail, name='detail'),
]

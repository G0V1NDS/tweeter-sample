from django.urls import path, include

from app.user import views as user_app_views


urlpatterns = [
    # System User Related URLs
    path('login/', view=user_app_views.user_login, name='user_login'),
    path('logout/', view=user_app_views.user_logout, name='user_logout'),
    path('details/', view=user_app_views.user_details, name='user_details'),
]

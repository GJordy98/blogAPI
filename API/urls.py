from .views import RegisterView, login_view
from django.urls import path
#from rest_framework.routers import DefaultRouter
#from .views import CommentaireViewSet


#router = DefaultRouter()


#router.register(r'Commentaire', CommentaireViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
]
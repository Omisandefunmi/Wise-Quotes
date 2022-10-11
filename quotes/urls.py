from rest_framework.routers import *
from quotes import views
from django.urls import path,include
from quotes.views import *



router = SimpleRouter()
router.register('quote', views.QuoteViewSet,basename="quote")

urlpatterns = [
    path('', include(router.urls)),
    path('api/generate_quote/', views.GenerateQuote.as_view()),

    
]


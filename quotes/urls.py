from rest_framework.routers import *
from quotes import views
from django.urls import path,include
from quotes.views import *


urlpatterns = [
    path('api/generate_quote/', views.GenerateQuote.as_view()),
    # path('api/display_quote/', views.DisplayQuote.as_view()),
    
]

router = SimpleRouter()
router.register('quote', views.QuoteViewSet,basename="quote")

urlpatterns = [
    path('', include(router.urls)),

    
]


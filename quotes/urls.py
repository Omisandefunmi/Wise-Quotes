from django.urls import path
from . import views

urlpatterns = [
    path('quoteslist/', views.QuoteList.as_view()),
    path('quotesdetail/<int:pk>/', views.QuoteDetail.as_view()),
]
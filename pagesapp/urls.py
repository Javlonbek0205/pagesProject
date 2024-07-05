from .views import HomepageView, AboutpageView
from django.urls import path
urlpatterns = [
  path('',HomepageView.as_view(), name='home'),
  path('about/',AboutpageView.as_view(), name='about')
]
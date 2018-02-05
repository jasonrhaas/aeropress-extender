from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('get_email/', views.get_email, name='get_email'),
    path('thanks/', views.thanks, name='thanks'),
    path('pricing/', views.pricing, name='pricing'),
    path('cart/', views.cart, name='cart'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

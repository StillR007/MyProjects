from django.urls import path
from .views import index, by_rubric, DbCreateView

urlpatterns = [
    path('add/', DbCreateView.as_view(), name='add'),
    path('', index, name='index'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
]

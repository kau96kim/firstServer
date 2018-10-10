from django.urls import path
from memo.views import MemoList, MemoDetail


urlpatterns = [
    path('', MemoList.as_view(), name='index'),
    path('<int:pk>/', MemoDetail.as_view(), name='detail'),
]

from django.urls import path
from django.views.generic.detail import DetailView

from .views import *
from .models import Photo

app_name = 'photo'
    # name space로 사용되는 값.
    # 템플릿에서 url 템플릿 태그를 사용할 때 이 값이 설정돼있으면 [앱이름:URL패턴이름] 형태로 사용 가능

urlpatterns = [
    path('', photo_list, name='photo_list'),
        # photo 앱의 메인 페이지로 지정한다는 뜻이다.
    path('deatil/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
        # path('deatil/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
        # 이걸로 view.py 에 class 지정 없이 가능하긴 하다.
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
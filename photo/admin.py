from django.contrib import admin

from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']   # 목록에 보일 필드를 설정한다. 모델의 필드를 선택하거나 별도 함수를 만들어 필드처럼 등록 가능.
    raw_id_fields = ['author']
        # ForeignKey 필드의 경우 연결된 모델의 객체 목록을 출력하고 선택해야되는데, 목록이 너무 길 경우 불편해진다.
        # 이 옵션으로 값을 써넣는 형태로 바뀌어 검색기능을 선택해 사용할 수 있다
    list_filter = ['created', 'updated', 'author']  # 필터 기능을 사용할 필드를 선택한다. 장고가 적절하게 필터 범위를 출력해준다.
    search_fields = ['text', 'created']     # 검색 기능을 통해 검색할 필드를 선택한다. ForeignKey 필드는 설저할 수 없다.
    ordering = ['-updated', '-created']     # 모델의 기본 정렬 값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값.

admin.site.register(Photo, PhotoAdmin)
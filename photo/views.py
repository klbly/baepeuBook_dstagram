from django.shortcuts import render

from .models import Photo 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def photo_list(request):    # 함수형 뷰, 클래스형 뷰와 달리 모든 기능을 직접 처리해야한다.
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})

# @login_required
# 로그인 필요 메뉴 지정 하는 방법은 두 가지다
    # @login_required 라고 class 위에 데코레이터를 붙이거나
    # LoginRequiredMixin, 라고 class 상속자 자리에 믹스드인을 넣거나
class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id 
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

# @login_required
        # 로그인 필요 메뉴 지정 하는 방법은 두 가지다
    # @login_required 라고 class 위에 데코레이터를 붙이거나
    # LoginRequiredMixin, 라고 class 상속자 자리에 믹스드인을 넣거나
class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

# @login_required
    # 로그인 필요 메뉴 지정 하는 방법은 두 가지다
    # @login_required 라고 class 위에 데코레이터를 붙이거나
    # LoginRequiredMixin, 라고 class 상속자 자리에 믹스드인을 넣거나
class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

# @login_required
    # 로그인 필요 메뉴 지정 하는 방법은 두 가지다
    # @login_required 라고 class 위에 데코레이터를 붙이거나
    # LoginRequiredMixin, 라고 class 상속자 자리에 믹스드인을 넣거나
class PhotoDetailView(LoginRequiredMixin, DetailView):
    model=Photo
    template_name='photo/detail.html'
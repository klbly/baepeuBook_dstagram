from django.contrib.auth.models import User 
from django import forms 

class RegistraterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
        # password는 fields에서 설정할 수 있지만, 종류가 CharField이기 때문에 별도의 Widget 옵션을 사용해 input 태그를 사용하려고 클래스 변수로 지정했다.
        # password2 필드도 만들어서 회원 가입시 비밀번호 재입력 기능을 구현행ㅆ다.

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']   # 입력 받을 필드 설정
    
    def clean_password2(self):
        # clean_필드명 형태의 메서드다: 이런 형태의 메서드는 각 필드의 clean 메서드가 호출된 후에 호출되는 메서드다
        # 꼭 cleaned_data에서 필드 값을 찾아서 사용해야한다. 이 값이 이전 단계까지 기본 유효성 검사같은 처리를 마친 값이기 때문이다.
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
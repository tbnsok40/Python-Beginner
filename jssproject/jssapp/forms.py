from django import forms
from .models import Jasosul

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasosul
        # fields = '__all__'
        fields = ('title', 'body',)  #모델과 필드, 두가지 인자를 받는다. 모델은 받고싶은 데이터, 필드는 원하는 부분만 인자로 선언/생성
            
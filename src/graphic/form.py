from django import forms
from math import *
from graphic.models import Graphic


class GraphicModuleForm(forms.ModelForm):
    function = forms.CharField(label='Функция',
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Введите функцию'
                               }
                               ))
    step = forms.IntegerField(label='Шаг',
                              widget=forms.NumberInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Шаг',
                              }))
    top_interval = forms.FloatField(label='Верний интервал',
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': '',
                                    }))
    bot_interval = forms.FloatField(label='Нижний интервал',
                                    widget=forms.NumberInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': '',
                                    }))

    class Meta:
        model = Graphic
        fields = ['function', 'step', 'bot_interval', 'top_interval']

    def clean_function(self):
        function = self.cleaned_data['function']
        y = []
        try:
            exec(f'def func(x):\n return {function}\ny.append(func(1))')
        except NameError:
            raise forms.ValidationError("Аргументом функции должна быть переменная 'x'")
        except ZeroDivisionError:
            raise forms.ValidationError("Деление на ноль!")
        return function

    def clean(self):
        cleaned_data = super(GraphicModuleForm, self).clean()
        bot_interval = cleaned_data.get("bot_interval")
        top_interval = cleaned_data.get("top_interval")

        if bot_interval >= top_interval:
            raise forms.ValidationError("Вверхний интервал не может быть меньше  нижнего ")
        return self.cleaned_data

    def clean_step(self):
        step = self.cleaned_data['step']
        if self.cleaned_data['step'] <= 0:
            return forms.ValidationError("Шаг не может быть меньше 0")
        return step
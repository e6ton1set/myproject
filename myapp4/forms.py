import datetime
from django import forms


class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_email(self):
        email: str = self.cleaned_data['email']

        if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birth_date = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(label="", min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Возраст'}))
    height = forms.FloatField(label="", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рост'}))
    birth_date = forms.DateField(label="", initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control',
                                                                                            'type': 'date', 'placeholder': 'Дата рождения'}))
    gender = forms.ChoiceField(label="", choices=[('M', 'Мужчина'), ('F', 'Женщина')],
                               widget=forms.Select(attrs={'class': 'check-input'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше сообщение'}))
    is_active = forms.BooleanField(label="Активировать сразу", required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))


class ImageForm(forms.Form):
    image = forms.ImageField()



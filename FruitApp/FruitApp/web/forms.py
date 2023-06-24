from django import forms

from .models import Profile, Fruit


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        # widgets = {
        #     'first_name': forms.CharField(attrs={'placeholder': 'First Name'}),
        #     'last_name': forms.CharField(attrs={'placeholder': 'Last Name'}),
        #     'email': forms.EmailField(attrs={'placeholder': 'Email'}),
        #     'password': forms.CharField(attrs={'placeholder': 'Password'}),
        #
        # }


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    pass


class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['password', 'email']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditForm(ProfileBaseForm):
    pass

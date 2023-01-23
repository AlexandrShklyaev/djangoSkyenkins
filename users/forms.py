from users.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Ведите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_name', 'email',)

    def clean_password2(self):  # check that two password entries match or not
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("пароли не совпадают!")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def as_p(self):
        return self._html_output(
            normal_row=u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
            error_row=u'%s',
            row_ender='</p>',
            help_text_html=u' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegistrationForm(UserCreationForm):
    # 使用内置 User：username 存学号，first_name 存完整姓名。
    first_name = forms.CharField(
        label="姓名", max_length=150,
        widget=forms.TextInput(attrs={"autocomplete": "name"}),
    )

    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name")
        labels = {"username": "学号"}
        help_texts = {"username": "作为登录账号使用；同一个学号只能注册一次。"}
        error_messages = {"username": {"unique": "这个学号已注册，请直接登录。"}}
        widgets = {"username": forms.TextInput(attrs={"autocomplete": "username"})}


class StudentLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "学号或密码不正确，请重新输入。",
        "inactive": "该账号当前无法登录。",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "学号"
        self.fields["username"].widget.attrs["autocomplete"] = "username"

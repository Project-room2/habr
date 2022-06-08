import hashlib
import random
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from userapp.models import User, UserProfile


# "This is a form that will be used to log users in."
#
# The first line of the class, class UserLoginForm(AuthenticationForm):, tells Django that the UserLoginForm class we're
# defining is a subclass of Django's AuthenticationForm class. This means that our UserLoginForm class will inherit all of
# the built-in AuthenticationForm functionality
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        """
        The function takes in a form class, and returns a new form class with the specified attributes
        """
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


# "This is a form that will be used to create a new user."
#
# The first line of the class is the name of the class. The name of the class is UserRegisterForm
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        """
        The function takes in a form, and for each field in the form, it sets the widget's class attribute to 'form-control
        py-4'
        """
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл. почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    def save(self, commit=True):
        """
        The function takes the user's email and a random salt and hashes them together to create a unique activation key

        :param commit: If True, then the changes to the object are saved to the database, defaults to True (optional)
        :return: The user object is being returned.
        """
        user = super().save()
        user.is_active = False
        user.avatar = 'users_avatar/default.jpg'
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()
        user.activation_key = hashlib.sha1(str(user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


# "This is a form that inherits from UserChangeForm, and adds an avatar field."
#
# The first line of the class is the most important. It tells Django that this form inherits from UserChangeForm. This
# means that all of the fields from UserChangeForm will be included in this form
class UserProfileForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'age')

    def __init__(self, *args, **kwargs):
        """
        We're overriding the default init function of the form and adding a class to all the fields
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-2'
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


# "This is a form that will be used to edit the UserProfile model."
#
# The Meta class tells Django which model should be used to create this form (model = UserProfile)
class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('gender','aboutMe')

    def __init__(self, *args, **kwargs):
        """
        The function takes in a form and adds the class 'form-control' to all the fields in the form
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
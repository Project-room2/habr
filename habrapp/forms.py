from django.forms import ModelForm, TextInput, Select

from mainapp.models import Habr
from ckeditor_uploader.fields import RichTextUploadingFormField


# рабочий вариант
class HabrEditForm(ModelForm):
    class Meta:
        model = Habr  # определяем, какая модель будет использоваться для создания формы
        fields = ('title', 'category', 'content')
        widgets = {
            'title': TextInput(attrs={'style': 'width: 1000px;', 'class': 'form-control', 'required': True}),
            'category': Select(attrs={'style': 'width: 200px;', 'class': 'form-control', 'required': True}),
            'content': RichTextUploadingFormField(
                # config_name="content-toolbar"
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            field.required = False

from django.forms import ModelForm, TextInput, Select

from mainapp.models import Habr
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField
from taggit.forms import TagWidget


# рабочий вариант
class HabrEditForm(ModelForm):
    class Meta:
        model = Habr  # определяем, какая модель будет использоваться для создания формы
        fields = ('title', 'category', 'content', 'tags')
        widgets = {
            'title': TextInput(attrs={'style': 'width: 100%', 'class': 'form-control', 'required': True}),
            'category': Select(attrs={'style': 'width: 50%', 'class': 'form-control', 'required': True}),
            'content': RichTextUploadingFormField(),
            'tags': TagWidget(attrs={'style': 'width: 100%', 'class': 'form-control', 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            field.required = False

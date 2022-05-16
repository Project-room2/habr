from django.forms import ModelForm, Textarea, TextInput, Select, Form

from mainapp.models import Habr
from ckeditor_uploader.fields import RichTextUploadingField, RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField, RichTextFormField


class CkEditorForm(Form):
    ckeditor_standard_example = RichTextFormField()
    ckeditor_upload_example = RichTextUploadingFormField(
        config_name="default"
    )

# рабочий вариант
class HabrEditForm(ModelForm):
    class Meta:
        model = Habr  # определяем, какая модель будет использоваться для создания формы
        fields = ('title', 'category', 'content')
        widgets = {
            'title': TextInput(attrs={'style': 'width: 800px;', 'class': 'form-control', 'required': True}),
            'category': Select(attrs={'style': 'width: 800px;', 'class': 'form-control', 'required': True}),
            'content': RichTextUploadingFormField(
                config_name="content-toolbar"
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # field.widget.attrs['class'] = 'form-control'
            field.required = False
        self.fields["content"].widget = CKEditorUploadingWidget(
            config_name="content-toolbar",
            extra_plugins=["someplugin", "anotherplugin"],
            external_plugin_resources=[
                (
                    "someplugin",
                    "/static/path/to/someplugin/",
                    "plugin.js",
                )
            ],
        )
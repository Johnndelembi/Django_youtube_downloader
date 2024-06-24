from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Div

class DownloadForm(forms.Form):
    url = forms.URLField(label="A unique Youtube Downloader like you've never seen before", widget=forms.TextInput(attrs={'placeholder': 'Enter YouTube URL'}),  max_length=200)
    format_choices = [
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    format = forms.ChoiceField(choices=format_choices, widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(DownloadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'url', 'format',
            Row(
                Div('email', css_class='col-md-6'),
            ),
        )

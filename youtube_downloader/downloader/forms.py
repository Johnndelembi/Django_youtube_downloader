from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='YouTube URL', max_length=200)
    format_choices = [
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    format = forms.ChoiceField(choices=format_choices, widget=forms.RadioSelect)

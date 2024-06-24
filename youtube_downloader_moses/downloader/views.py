from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytube import YouTube
from .forms import DownloadForm
import os

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            download_format = form.cleaned_data['format']
            yt = YouTube(url)

            if download_format == 'video':
                stream = yt.streams.get_highest_resolution()
                file_extension = 'mp4'
            else:
                stream = yt.streams.filter(only_audio=True).first()
                file_extension = 'mp3'

            filename = f"{'freebie_downloads'}.{file_extension}"
            stream.download(output_path='downloads', filename=filename)
            file_path = os.path.join('downloads', filename)
            
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = f'attachment; filename={filename}'
                return response

    else:
        form = DownloadForm()

    return render(request, 'downloader/home.html', {'form': form})


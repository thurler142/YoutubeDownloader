from pytube import YouTube


link = input('Cole o link do video: ')

YouTube (link)
video = YouTube(link)
video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


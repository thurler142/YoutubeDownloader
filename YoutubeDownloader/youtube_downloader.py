from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg


sg.theme('Reddit')
layout = [
    [sg.Text('URL', auto_size_text=True), ],
    [sg.InputText(key = 'link')],
    [sg.Button('Baixar', auto_size_button = True)]
]
window = sg.Window('Minha Janela', layout)
def YTDownload ():
    event, values = window.read()
    link = values['link']
    video = YouTube(link)
    video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
YTDownload()  

while True:
    event, values = window.read()
    if event == 'Baixar':
        YTDownload()
        sg.popup('Baixado com Sucesso!')
        break

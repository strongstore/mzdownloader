from pytube import YouTube
from pytube.cli import on_progress
link = input("Enter Video Link: ")
video = YouTube(link, on_progress_callback=on_progress)
def finish():
    print('Download Done!')
print("Made by: Muhammad Zakarya")
stream = video.streams
if '1080p' in str(stream) and '720p' in str(stream) and '480p' in str(stream) and '360p' in str(stream) and '240p' in str(stream) and '144p' in str(stream):
    print('Quality 1 => 1080p')
    print('Quality 2 => 720p')
    print('Quality 3 => 480p')
    print('Quality 4 => 360p')
    print('Quality 5 => 240p')
    print('Quality 6 => 144p')
    qual = input('Choose quality to download: ')
    if qual == '1':
        stream.filter(res='1080p').first().download()
    elif qual == '2':
        stream.filter(res='720p').first().download()
    elif qual == '3':
        stream.filter(res='480p').first().download()
    elif qual == '4':
        stream.filter(res='360p').first().download()
    elif qual == '5':
        stream.filter(res='240p').first().download()
    elif qual == '6':
        stream.filter(res='144p').first().download()
elif '720p' in str(stream) and '480p' in str(stream) and '360p' in str(stream) and '240p' in str(stream) and '144p' in str(stream):
    print('Quality 1 => 720p')
    print('Quality 2 => 480p')
    print('Quality 3 => 360p')
    print('Quality 4 => 240p')
    print('Quality 5 => 144p')
    qual = input('Choose quality to download: ')
    if qual == '1':
        stream.filter(res='720p').first().download()
    elif qual == '2':
        stream.filter(res='480p').first().download()
    elif qual == '3':
        stream.filter(res='360p').first().download()
    elif qual == '4':
        stream.filter(res='240p').first().download()
    elif qual == '5':
        stream.filter(res='144p').first().download()
elif '480p' in str(stream) and '360p' in str(stream) and '240p' in str(stream) and '144p' in str(stream):
    print('Quality 1 => 480p')
    print('Quality 2 => 360p')
    print('Quality 3 => 240p')
    print('Quality 4 => 144p')
    qual = input('Choose quality to download: ')
    if qual == '1':
        stream.filter(res='480p').first().download()
    elif qual == '2':
        stream.filter(res='360p').first().download()
    elif qual == '3':
        stream.filter(res='240p').first().download()
    elif qual == '4':
        stream.filter(res='144p').first().download()
elif '360p' in str(stream) and '240p' in str(stream) and '144p' in str(stream):
    print('Quality 1 => 360p')
    print('Quality 2 => 240p')
    print('Quality 3 => 144p')
    qual = input('Choose quality to download: ')
    if qual == '1':
        stream.filter(res='360p').first().download()
    elif qual == '2':
        stream.filter(res='240p').first().download()
    elif qual == '3':
        stream.filter(res='144p').first().download()
elif '240p' in str(stream) and '144p' in str(stream):
    print('Quality 1 => 240p')
    print('Quality 2 => 144p')
    qual = input('Choose quality to download: ')
    if qual == '1':
        stream.filter(res='240p').first().download()
    elif qual == '2':
        stream.filter(res='144p').first().download()

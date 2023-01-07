from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error while downloading the video")
    print("Downloaded")

link = input("Enter the youtube link. URL: ")
Download(link)
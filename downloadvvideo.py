import pytube
print ('Download video from web by python')
url = input ('Enter video url :')
pytube.YouTube(url).streams.get_highest_resolution().download('pythonproject4')

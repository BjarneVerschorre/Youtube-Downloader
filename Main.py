import youtube_dl
import urllib.request
import re
import string

def validTitle(title: str) -> bool:
	return title != "\n" and string.ascii_letters not in title
def findUrl(seachTerm: str ) -> str:
	html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + seachTerm.replace(" ","+"))
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	return "https://www.youtube.com/watch?v=" + video_ids[0]
def download(url: str) -> None:
	video_info = youtube_dl.YoutubeDL().extract_info( url = url, download = False )
	options = {
		'format': 'bestaudio/best',
		'keepvideo': False,
		'outtmpl': f"Downloads/{video_info['title']}.mp3",
	}

	with youtube_dl.YoutubeDL(options) as music:
		music.download([video_info['webpage_url']])
def removeLine(text: str) -> None:
	with open('Titles.txt', 'r') as fr:
		lines = fr.readlines()
	 
		with open('Titles.txt', 'w') as fw:
			for line in lines:
				if line.strip('\n') != text:
					fw.write(line)

def Main() -> None:
	with open("Titles.txt","r") as f:
		for line in f:
			if not validTitle(line):
				continue

			title = line.strip("\n")
			url = findUrl(title)
			download(url)
			removeLine(title)


if __name__ == "__main__":
	Main()
		

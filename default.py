import sys
import urllib.request
from bs4 import BeautifulSoup
import xbmcplugin
import xbmcgui

base_url = 'http://circleftp.net/'  # or ICC FTP

def list_movies():
    response = urllib.request.urlopen(base_url)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith(('.mp4', '.mkv', '.avi')):
            title = link.text.strip()
            url = base_url + href if not href.startswith('http') else href
            li = xbmcgui.ListItem(label=title)
            li.setProperty('IsPlayable', 'true')
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    list_movies()

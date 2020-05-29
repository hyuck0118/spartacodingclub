import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

musics = soup.select('#body-content > div.newest-list > div.music-list-wrap > table > tbody > tr')

# musics (tr 들) 의 반복문 돌리기
for music in musics:
    # rank gives the number of steps also => need to fix
    ranks = music.select_one('td.number').text
    rank_change = music.select_one('td.number > span').text
    rank_num = ranks.strip(rank_change)
    rank_num_only = rank_num.strip()

    title = music.select_one('td.info > a.title.ellipsis').text
    title_clean = title.strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text

    print(rank_num_only, title_clean, artist)

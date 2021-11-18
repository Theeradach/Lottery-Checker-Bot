from bs4 import BeautifulSoup
import requests
from datetime import datetime
import emoji
from modules.LineNotify import LineNotify

def checkLotto():
    today = datetime.today()
    date = f"{today.day}{today.month}{today.year + 543}"
    url = "https://news.sanook.com/lotto/"
    res = requests.get(url)
    res.encoding = "utf-8"

    if res.status_code == 200:
        soup = BeautifulSoup(res.content, 'html.parser')
        title = soup.find("h1", {"class": "snvh"})
        firstWinner = soup.find("strong", {"class": "lotto__number lotto__number--first"})
        winThreeNumbers = soup.find_all("b", {"class": "lotto__number lotto__number--three"})
        winTwoNumbers = soup.find_all("strong", {"class": "lotto__number"})

        msg = f"""
            \U0001F3D8  {title.string}
            \U0001F4B0 รางวัลที่ 1    : {firstWinner.string}
            \U0001F4B4 เลขหน้า 3 ตัว : {winThreeNumbers[0].string} {winThreeNumbers[1].string}
            \U0001F4B5 เลขท้าย 3 ตัว : {winThreeNumbers[2].string} {winThreeNumbers[3].string}
            \U0001FA99 เลขท้าย 2 ตัว : {winTwoNumbers[1].string}
            \U0001F30D ตรวจหน้าเว็บ : {url}check/{date}
        """
        print(msg)
        LineNotify().sendMessage(msg)
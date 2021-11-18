# USER GUIDE

`Lottery Checker Bot`
- บอทสำหรับตรวจสอบ lottery ประเทศไทย จากเว็ป https://news.sanook.com/lotto/

Example Message
```
    🏘  ตรวจหวย งวด 16 พ.ย. 64
    💰 รางวัลที่ 1    : 032761
    💴 เลขหน้า 3 ตัว : 648 471
    💵 เลขท้าย 3 ตัว : 844 245
    🪙 เลขท้าย 2 ตัว : 57
    🌍 ตรวจหน้าเว็บ : https://news.sanook.com/lotto/check/16112564
```

## INSTALLATION GUIDE
- Prequision
  1. Login to Line and generate Line Token though `https://notify-bot.line.me/`
  2. Clone project respository 

```
    git clone https://github.com/Theeradach/Lottery-Checker-Bot.git
```

### Project Environment Setup Guide
1. Install python3 & pip
2. Install required python's packages

```
    pip install -r requirement.txt 
```

3. Copy `.env.example` to `.env`
4. Input Line Token in `.env` file 
5. How to Run Bot 

```
    python3 main.py
```
# Gorky
[![Maintenance](https://img.shields.io/badge/python-3.9-green.svg)](https://GitHub.com/ericgans/Gorky)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/ericgans/Gorky/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


Gorky is Google Dorker tools that can help you to grab website lists from Google Search.<br>
Gorky will save results with protocol (http/https) and domain only.<br>
Gorky will not save result if containing one of blacklist domain in blacklist.txt.<br>
Gorky only grab result in first page and second page on Google result. Why ? i'm too lazy.<br>

<br>

# Installation
 You can download as zip or using git :
>git clone https://github.com/ericgans/Gorky

Install BeautifulSoup4 using this command :
> pip install beautifulsoup4
<br>


# Before Start Using Gorky
Before Start Using Gorky you need to grab your cookies from your browser and save it in ***Cookies.txt*** <br>
Before start Gorky Make sure you have file named result.txt (even the contents of the file are empty)<br>
You can watch me Grab the cookies in [this video](https://youtube.com)

# Usage
After you put you cookies into ***Cookies.txt*** , now you can start Gorky.<br>
And remember to save your google dork list in the same dir.
> python gorky.py

![Image of Yaktocat](https://raw.githubusercontent.com/ericgans/Gorky/main/Screenshots.bmp)

<br>

# How about Google reCaptcha ?
Gorky can detect google recaptcha, but you need to solve recaptcha manual.<br>
If Gorky gives Google reCaptcha warning ,open google.com in your browser and search anything, solve Google Captcha and then grab your cookies from browser again and rewrite into ***Cookies.txt*** .

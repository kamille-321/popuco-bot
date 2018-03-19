# -*- coding: utf-8 -*-

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from libs import my_functions           # 外部関数の読み込み



@respond_to('てんき')
def weather(message):
    import urllib
    import json

    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    city_id = '130010'
    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    title = jsonfile['title']
    telop = jsonfile['forecasts'][0]['telop']
    lowest_temp  = jsonfile['forecasts'][0]['temperature']['min']['celsius']
    highest_temp = jsonfile['forecasts'][0]['temperature']['max']['celsius']
    telop_icon = ''

    if telop.find('雪') > -1:
        telop_icon = ':showman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thinder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'
    text = title + '\n' + telop + telop_icon + '　' + highest_temp + ' / ' + lowest_temp
    message.send(text)

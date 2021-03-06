# -*- coding: utf-8 -*-
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
from time         import sleep
import os

from libs import my_functions           # 外部関数の読み込み

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')      @発言者名: string でメッセージを送信
# message.send('string')       string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                              文字列中に':'はいらない

github_url  = os.environ["GITHUB_URL"]
issue_url   = os.environ["ISSUE_URL"]
pr_url      = os.environ["PR_URL"]

@respond_to('github')
def mention_func(message):
    message.reply(github_url)

@respond_to('issue')
def mention_func(message):
    message.reply(issue_url)

@respond_to('pr')
def mention_func(message):
    message.reply(pr_url)

@respond_to('さては')
def mention_func(message):
    message.reply('アンチだなオメー')

@respond_to('おはよう')
def mention_func(message):
    message.reply('今日も１日がんばるぞい！٩( ‘ω’ )و')

@respond_to('おそよう')
def mention_func(message):
    message.reply('俺はこういう人間だ！俺はこういう人間！')

@respond_to('かえる')
def mention_func(message):
    message.reply('エサヒィ～スープゥードゥラァ～イ！')

@respond_to('だれ')
def mention_func(message):
    message.reply('私だよ!!!!!!')
    message.reply(':popte10:')

@respond_to('どのくらい好きか教えて')
def mention_func(message):
    message.reply('いっぱいちゅき♡')
    message.reply(':popte15:')

angry_count = 1
@respond_to('えいえい、怒った')
def mention_func(message):
    global angry_count

    if angry_count == 1:
        message.reply('怒ってないよ')
        angry_count += 1
    elif angry_count < 3:
        message.reply('怒ってないよ')
        angry_count += 1
    elif angry_count == 3:
        message.reply('怒っ.....')
        message.reply(':popte14:')
        angry_count = 1


@respond_to('しね')
def mention_func(message):
    message.reply('ハイクソー')
    sleep(5)
    message.reply('クソクソクソクソクソクソクソクソクソクソクソクソクソクソクソクソクソクソ')


@respond_to('生きてる？')
def mention_func(message):
    message.reply('もしもしポリスメン？')

@default_reply()
def default(message):
    import requests
    import json
    import types

    KEY = os.environ.get("DOCOMO_API_KEY")

    #エンドポイントの設定
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=REGISTER_KEY'
    url = endpoint.replace('REGISTER_KEY', KEY)
    text = message.body['text']

    payload = {'utt' : text, 'context': ''}
    headers = {'Content-type': 'application/json'}

    #送信
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    #jsonの解析
    response = data['utt']
    context = data['context']

    #表示
    message.reply('%s' % response)


@listen_to('おすおす')
def listen_func(message):
    message.send('誰かがおすおすと投稿したようだ')
    message.reply('君だね？')

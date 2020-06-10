from slacker import Slacker
import weather
 
def main():
 
    dic_weather = {
        '晴れ' : 'sunny',
        '曇り' : 'cloud',
        '雨' : 'rain_cloud',
        '雪' : 'snow_cloud',
        '曇時々晴' : 'barely_sunny',
    }
 
    dic_date = {
        '今日': 0,
        '明日': 1,
        '明後日': 2
    }
 
    w = weather.get_weather(130010)
    t = w['forecasts'][dic_date['今日']]
    telop = t['telop']
 
    # 辞書にない天気が来たら絵文字に空文字を設定する
    if telop in dic_weather:
        emoji = ':' + dic_weather[telop] + ':'
    else:
        emoji = ""
    # テキストファイル読み込み
    f = open('../token.txt', 'r')
    token = f.read()
    # print(token)
    # APIトークンを設定する
    slack = Slacker(token)
    # Slackにメッセージを送信する
    slack.chat.post_message('agenda-bot-test', '今日の天気は%sです%s' % (telop, emoji), as_user=True)
 
if __name__ == "__main__":
    main()
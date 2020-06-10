import json
import requests
 
def get_weather(city_number):
    # 天気のURL設定 city_numberには都市番号を指定
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s" % city_number
 
    # URLを取得
    response = requests.get(url)
    # URL取得結果のチェック
    response.raise_for_status()
    # 天気データを読み込む
    weather_data = json.loads(response.text)
 
    return(weather_data)
 
# テストコード
def main():
    # 東京の天気を取得する(130010)は東京の都市番号
    w = get_weather(130010)
    t = w['forecasts'][0]
 
    print(t['dateLabel']) # 今日
    print(t['date']) # 日付
    print(t['telop']) # 天気
 
if __name__ == "__main__":
    main()
# テキストファイル読み込み
f = open('../token.txt', 'r')
token = f.read()
print(token)

# トークン
API_TOKEN = token

# 応答サンプル
DEFAULT_REPLY = 'は？'

# プラグイン
PULUGINS = ['plugins']

f.close()
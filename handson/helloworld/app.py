# flaskパッケージのFlaskクラスをインポート
from flask import Flask

# FLaskクラスのインスタンスを作成
app = Flask(__name__)

# Flaskクラスのインスタンス（app）のrouteデコレータを使い，/というURLに対しての処理を追加
@app.route('/')
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)

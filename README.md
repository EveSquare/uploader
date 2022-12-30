# -p-

## セットアップ
```
virtualenv .venv
. venv/bin/activate
pip instal -r requirements.txt
cp .env.example .env
export PATH = $PATH:＜クローンしたリポジトリのディレクトリ＞
```

## API接続のキー取得
以下のサイトを参考に`client-id`と`client-secret`を取得し`.env`に記述．
https://pisuke-code.com/web-basic-usage-of-imgur-api/

## 使い方
```
uploader ＜ファイルのパス：Macの場合ドロップもできる＞
```
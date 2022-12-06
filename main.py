import os
import sys

import pyperclip
from dotenv import load_dotenv
from imgurpython import ImgurClient

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# 画像パスの指定
args = sys.argv
image_path = args[1]

print("image_path: " + image_path)

client = ImgurClient(client_id, client_secret)

# 画像アップロード
print("# uploading ...🔖")
image = client.upload_from_path(image_path, config=None, anon=True)

# 画像リンク表示
print("# upload done✅")
print(image["link"])
pyperclip.copy(image["link"])
print("クリップボード⌨にコピーしたーお㊢")
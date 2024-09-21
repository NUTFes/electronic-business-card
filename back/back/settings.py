import os
from pathlib import Path

# データベース設定
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_HOST', 'mydb'),  # ここでホスト名が環境変数から取得されているか確認
        'PORT': 3306,
    }
}

ALLOWED_HOSTS = ['*']

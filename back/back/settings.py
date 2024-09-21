import os
from pathlib import Path

# BASE_DIR: プロジェクトのベースディレクトリを定義
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: セキュリティキー (本番環境では強力なキーを設定)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-placeholder-key')

# DEBUG: デバッグモード (本番環境では必ず False にする)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS: 許可するホストのリスト (本番環境では具体的なホストを指定)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# アプリケーション定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'back',  # ここで自分のアプリ（back）を追加
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # これを追加
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# フロントエンドからのアクセスを許可する
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",  # Next.js フロントエンドが実行されているホスト
]


# URLconf: ルートURLの設定
ROOT_URLCONF = 'back.urls'

# テンプレート設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI アプリケーション設定
WSGI_APPLICATION = 'back.wsgi.application'

# データベース設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'mydatabase'),
        'USER': os.environ.get('MYSQL_USER', 'myuser'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'mypassword'),
        'HOST': os.environ.get('MYSQL_HOST', 'mydb'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}

# 認証設定 (パスワードバリデータ)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ロケール設定
LANGUAGE_CODE = 'ja'

# タイムゾーン設定
TIME_ZONE = 'Asia/Tokyo'

# 国際化の設定
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静的ファイルの URL 設定
STATIC_URL = '/static/'

# 静的ファイルの配置場所
STATICFILES_DIRS = [BASE_DIR / 'static']

# デフォルトの自動フィールド
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-a7p9^*5qll0ppkal+hinzsfv!dv)kdsk7gh=r@fcxjh*%w_j#e'

DEBUG = False


# =========================
# HOSTS
# =========================
ALLOWED_HOSTS = [
    "oil-monitor-d8va.onrender.com",
    "fuelblack-market-protector.vercel.app",
]


# =========================
# APPS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    "corsheaders",
    "django_crontab",
    "whitenoise",
    "backend",
]


# =========================
# MIDDLEWARE (IMPORTANT ORDER)
# =========================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# CORS (FULL OPEN FIX)
# =========================
CORS_ALLOW_ALL_ORIGINS = True


# =========================
# CSRF (safe for dev)
# =========================
CSRF_TRUSTED_ORIGINS = [
    "https://oil-monitor-d8va.onrender.com",
    "https://fuelblack-market-protector.vercel.app",
    "http://localhost:3000",
    "http://localhost:3003",
]


ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

CRONJOBS = [
    ('*/3 * * * *', 'backend.cron.cleanup_inventory_logs'),
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# """
# Django settings for core project.
# """

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent


# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-a7p9^*5qll0ppkal+hinzsfv!dv)kdsk7gh=r@fcxjh*%w_j#e'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# # =========================
# # ALLOWED HOSTS
# # =========================
# ALLOWED_HOSTS = [
#     "oil-monitor-d8va.onrender.com",
#     "fuelblack-market-protector.vercel.app",
#     "localhost",
#     "127.0.0.1",
# ]


# # =========================
# # CSRF SETTINGS
# # =========================
# CSRF_TRUSTED_ORIGINS = [
#     "https://oil-monitor-d8va.onrender.com",
#     "https://fuelblack-market-protector.vercel.app",
#     "http://localhost:3000",
#     "http://localhost:3003",
#     'https://*.127.0.0.1'
# ]


# # =========================
# # APPLICATIONS
# # =========================
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     # Third party
#     "rest_framework",
#     "corsheaders",

#     # Local apps
#     "backend",
# ]


# # =========================
# # MIDDLEWARE (IMPORTANT ORDER)
# # =========================
# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware",  # MUST be on top

#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',

#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# # =========================
# # CORS CONFIG (IMPORTANT for React)
# # =========================
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:3003",
#     "https://fuelblack-market-protector.vercel.app",
# ]

# CORS_ALLOW_CREDENTIALS = True


# ROOT_URLCONF = 'core.urls'


# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'core.wsgi.application'


# # =========================
# # DATABASE
# # =========================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # =========================
# # PASSWORD VALIDATION
# # =========================
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]


# # =========================
# # INTERNATIONALIZATION
# # =========================
# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Dhaka'

# USE_I18N = True

# USE_TZ = True


# # =========================
# # STATIC FILES
# # =========================
# STATIC_URL = 'static/'


"""
Django settings for core project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY
# =========================
SECRET_KEY = 'django-insecure-a7p9^*5qll0ppkal+hinzsfv!dv)kdsk7gh=r@fcxjh*%w_j#e'

DEBUG = True  # production এ False করতে হবে


# =========================
# HOSTS
# =========================
ALLOWED_HOSTS = [
    "oil-monitor-d8va.onrender.com",
    "fuelblack-market-protector.vercel.app",
    "localhost",
    "127.0.0.1",
]


# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    "rest_framework",
    "corsheaders",

    # Local apps
    "backend",
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # MUST be first

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================
# CORS SETTINGS (React/Vercel FIX)
# =========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3003",
    "https://fuelblack-market-protector.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True


# =========================
# CSRF SETTINGS
# =========================
CSRF_TRUSTED_ORIGINS = [
    "https://oil-monitor-d8va.onrender.com",
    "https://fuelblack-market-protector.vercel.app",
    "http://localhost:3000",
    "http://localhost:3003",
]


# =========================
# ROOT CONFIG
# =========================
ROOT_URLCONF = 'core.urls'


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


WSGI_APPLICATION = 'core.wsgi.application'


# =========================
# DATABASE (SQLite for now)
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = 'static/'
"""
Django settings for api_cliente project.
"""
from pathlib import Path

# --- Configuração Básica ---
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t$c#&vj*0!&5+h_g8-b3d^d9@q2i(v*7(n6_k03(c%v7b#0d-@' 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
ROOT_URLCONF = 'api_cliente.urls'

# --- Aplicações Instaladas ---
INSTALLED_APPS = [
    # Módulos Padrão do Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Apps de Terceiros
    'rest_framework', # Framework principal da API
    
    # Seu App
    'cliente',
]

# --- Middleware (Processamento de Requisições) ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Templates (CORREÇÃO do erro admin.E403) ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True, # Permite que o Django Admin encontre seus templates
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

WSGI_APPLICATION = 'api_cliente.wsgi.application'


# --- Configuração do Banco de Dados ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'api_cliente',      
        'USER': 'root', 
        'PASSWORD': '@Samsao2025@', 
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", 
            'charset': 'utf8mb4',
        }
    }
}

# --- Configuração do Django REST Framework (PÚBLICA) ---
REST_FRAMEWORK = {
    # Nenhuma classe de autenticação padrão é definida.
    # A permissão pública é controlada na view (permission_classes = [AllowAny]).
}


# --- Validação de Senha (Padrão Django) ---
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


# --- Regionalização ---
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Manaus'
USE_I18N = True
USE_TZ = True


# --- Arquivos Estáticos ---
STATIC_URL = 'static/'

# --- Chave Primária Padrão ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
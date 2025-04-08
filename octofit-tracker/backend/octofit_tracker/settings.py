# Update INSTALLED_APPS to reference the correct app path
INSTALLED_APPS = [
    'octofit-tracker.backend.octofit_tracker',
    'rest_framework',
    'corsheaders',
    'octofit_tracker.apps.OctofitTrackerConfig',
]

# Define the MIDDLEWARE list if not already defined
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add CORS headers middleware
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

# Allow all origins for now (adjust as needed for production)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
]
ALLOWED_HOSTS = ['*']

# Configure database to use djongo
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}
import os
# Django settings for djnyc_multiwidget project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

PROJECT_ROOT = os.path.dirname(__file__)
DATABASES = {                                                                    
    'default': {                                                                 
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'dev.db'), # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.                
        'PASSWORD': '',                  # Not used with sqlite3.                
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }                                                                            
} 

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.  
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a          
# trailing slash.                                                                
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"      
MEDIA_URL = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd#zj4%@w63h*xj7$32@h_ubz6@5#0n%0f518)&!e%w5cbo@*!='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (                                                             
    'django.template.loaders.filesystem.Loader',                                 
    'django.template.loaders.app_directories.Loader',                            
)    

MIDDLEWARE_CLASSES = (                                                           
    'django.middleware.common.CommonMiddleware',                                 
    'django.contrib.sessions.middleware.SessionMiddleware',                      
    #'django.middleware.csrf.CsrfViewMiddleware',                                 
    'django.contrib.auth.middleware.AuthenticationMiddleware',                   
    'django.contrib.messages.middleware.MessageMiddleware', 
)

ROOT_URLCONF = 'django_multiwidget_demo.urls'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), "templates"))

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'djnycapp'
)

if DEBUG:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "/static")
#    STATICFILES_DIRS = (                                                             
#        # Put strings here, like "/home/html/static" or "C:/www/django/static".      
#        # Always use forward slashes, even on Windows.                               
#        # Don't forget to use absolute paths, not relative paths.                    
#        os.path.join(PROJECT_ROOT, "/static"),
#    )
    STATICFILES_FINDERS = (                                                          
        'django.contrib.staticfiles.finders.FileSystemFinder',                       
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',                   
        #    'django.contrib.staticfiles.finders.DefaultStorageFinder',                  
    ) 
    INSTALLED_APPS += (
        'django.contrib.staticfiles',
    )

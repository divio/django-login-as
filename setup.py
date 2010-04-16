from setuptools import setup, find_packages

version = __import__('login_as').__version__

setup(
    name = 'django-login-as',
    version = version,
    description = 'Django Login As any user',
    author = 'Jonas Obrist',
    author_email = 'jonas.obrist@divio.ch',
    url = 'http://github.com/ojii/django-login-as',
    packages = find_packages(),
    package_data={
        'login_as': [
            'templates/login_as/*.html',
        ]
    },
    zip_safe=False,
)
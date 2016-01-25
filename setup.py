from setuptools import find_packages, setup

setup(
    name='django_stackoverflow_trace',
    version='0.0.4',
    packages=find_packages(),
    url='https://github.com/emre/django-stackoverflow-trace',
    license='MIT',
    author='Emre Yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A custom Django technical error template that puts a stackoverflow '
                'search link above the related exception message.',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)
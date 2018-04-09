import os

from setuptools import setup


f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name = 'django-random-cats',
    version = '0.1',
    packages = ['cats'],
    include_package_data = True,
    install_requires = [line for line in read('requirements.txt').split('\n')
                        if line and not line.startswith('#')],
    license = 'MIT License',
    long_description = readme,
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

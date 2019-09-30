try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Useful in creating and storing passwords',
    'author': 'Kenan Al-Shamie',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ken.alshamie@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'string', 'random'],
    'packages': ['Create Encrypt Store'],
    'scripts': ['docs/password_gen',
                'docs/caesar_shift'],
    'name': 'Create Encrypt Store'
}

setup(**config)
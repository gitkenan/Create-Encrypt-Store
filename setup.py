try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Useful in creating and storing passwords',
    'author': 'Kenan Al-Shamie',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/gitkenan/Create-Encrypt-Store',
    'author_email': 'ken.alshamie@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'string', 'random', 'time'],
    'packages': ['Create Encrypt Store'],
    'scripts': ['docs/password_gen',
                'docs/caesar_shift'
                'docs/create_encrypt_store'],
    'name': 'Create Encrypt Store'
}

setup(**config)
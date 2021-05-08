from distutils.core import setup
import os

def read(fname):
    """Utility function to get README.rst into long_description.

    ``long_description`` is what ends up on the PyPI front page.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'emoji_flags',
  packages = ['emoji_flags'],
  version = '0.2.0',
  description = 'Python Package for Country Flag Emojis.',
  author = 'Denis Kartashov',
  author_email = 'None',
  url = 'https://github.com/dEN5-tech/emoji_flags/',
  download_url = 'https://github.com/dEN5-tech/emoji_flags/archive/refs/tags/0.1.1.tar.gz',
  keywords = ['geolocation', 'flags', 'emoji'],
  long_description=read('README'),
  classifiers = [],
)

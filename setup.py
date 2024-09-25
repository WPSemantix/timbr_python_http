import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='pytimbr_api',
  version='1.0.2',
  author='timbr',
  author_email='contact@timbr.ai',
  description='Timbr REST API connector',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/WPSemantix/timbr_python_http',
  download_url = 'https://github.com/WPSemantix/timbr_python_http/archive/refs/tags/v1.0.2.tar.gz',
  project_urls={
    "Bug Tracker": "https://github.com/WPSemantix/timbr_python_http/issues"
  },
  license='MIT',
  packages=['pytimbr_api'],
  install_requires=[],
  package_data={},
  keywords = [
    'timbr',
    'timbr-http',
    'timbr-https',
    'timbr-rest',
    'timbr-api',
    'timbr-rest-api',
    'timbr-connector',
    'PyTimbrRestAPI',
    'PyTimbr',
    'pytimbrapi',
    'PyTimbrAPI',
    'pytimbr_api',
    'PyTimbr_API',
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)

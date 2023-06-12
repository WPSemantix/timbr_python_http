import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name='timbr_rest_api',
  version='1.0.0',
  author='timbr',
  author_email='contact@timbr.ai',
  description='Timbr REST API connector',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/WPSemantix/timbr_http',
  project_urls={
    "Bug Tracker": "https://github.com/WPSemantix/timbr_http/issues"
  },
  license='MIT',
  packages=['timbr_rest_api'],
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

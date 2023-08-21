from setuptools import setup, find_packages
import pathlib

base = pathlib.Path(__file__).parent.resolve()
# Get the long description from the README file
long_description = (base / "README.md").read_text(encoding="utf-8")

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  "Topic :: Software Development :: Libraries :: Python Modules",
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
]
 
setup(
  name='python_flipkart_scraper',
  version='1.0.0',
  description='Scrap Product Data from Flipkart',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/sannjayy/python_flipkart_scraper',  
  author='Sanjay Sikdar',
  author_email='me@sanjaysikdar.dev',
  license='MIT', 
  classifiers=classifiers,
  keywords='python, scraper, flipkart scraper', 
  packages=find_packages(where="src"),
  python_requires=">=3.9, <4",   
  package_dir={'':'src'},
  install_requires=[
    'progress==1.6',
    'py-essentials==1.4.12',
  ],
  project_urls={
    "Bug Reports": "https://github.com/sannjayy/python_flipkart_scraper/issues",
    "Funding": "https://www.paypal.com/paypalme/znasofficial",
    "Say Thanks!": "https://saythanks.io/to/sannjayy",
    "Source": "https://github.com/sannjayy/python_flipkart_scraper/",
  },
)
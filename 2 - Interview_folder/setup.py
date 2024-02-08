from setuptools import find_packages
from setuptools import setup


with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='nba_predict',
      version="0.0.1",
      description="nba_predict",
      license="MIT",
      author="Arthur DUBOIS",
      author_email="arthurdubsm@gmail.com",
      #url="https://github.com/lewagon/taxi-fare",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)

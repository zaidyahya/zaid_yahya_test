from setuptools import setup, find_packages

setup(name='Version Comparator',
      version='0.1',
      url='https://github.com/zaidyahya/Ormuco/tree/master/q2',
      license='MIT',
      author='zaidyahya',
      author_email='zaid.yahya@mail.mcgill.ca',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
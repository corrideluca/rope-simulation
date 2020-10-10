from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='F2Depine',
  version='0.0.6',
  description='Para resolver ejercicios de F2',
  long_description=open('README.md').read(),
  url='https://github.com/Corri3141/F2Depine',  
  author='Corrado De Luca',
  author_email='corrideluca@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='f2depine', 
  packages=find_packages(),
  install_requires=[
    "certifi==2020.6.20",
    "cycler==0.10.0",
    "kiwisolver==1.2.0",
    "matplotlib==3.3.2",
    "numpy==1.19.2",
    "Pillow==7.2.0",
    "pyparsing==2.4.7",
    "python-dateutil==2.8.1",
    "scipy==1.5.2",
    "six==1.15.0",] 
)
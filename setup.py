#from distribute_setup import use_setuptools
#use_setuptools()

from setuptools import setup, find_packages
from os.path import dirname, join

here = dirname(__file__)
setup(
    name='btchip-python',
    version='0.1.5',
    author='BTChip',
    author_email='contact@btchip.com',
    description='Python library to communicate with BTChip dongle',
    long_description=open(join(here, 'README.md')).read(),
    packages=find_packages(),
    install_requires=['pyusb>=1.0.0b1'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
	'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Windows',
	'Operating System :: MacOS :: MacOS X'
    ]
)


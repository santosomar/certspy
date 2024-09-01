from setuptools import setup, find_packages

setup(
    name='certspy',
    version='0.9.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'certspy=certspy.certspy:main',  
        ],
    },
    author='Omar Santos',
    author_email='santosomar@gmail.com',
    description='A Python client for the crt.sh website to retrieve subdomains information',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santosomar/certspy',
    license='BSD 3-Clause License',
)

from setuptools import setup, find_packages

setup(
    name='certspy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'certspy=certspy.yourscript:main',  # Remember to replace 'yourscript' with the actual script file name
        ],
    },
    author='Omar Santos',
    description='A Python client for the crt.sh website to retrieve subdomains information',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/santosomar/certspy',
    license='BSD 3-Clause License',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
    ],
)

from setuptools import setup, find_packages

setup(
    name='weather-dashboard-demo',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'requests',
        'python-dotenv',
    ],
)

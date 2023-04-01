from setuptools import setup, find_packages

setup(
    name='PythonPackagingTest1SN',
    version='1.0',
    author='Sri N S R Nem',
    description='A brief synopsis of the project',
    long_description='A much longer explanation of the project and helpful resources',
    url='https://github.com/srinivasnemani/PythonPackagingTest1',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=find_packages(include=['PythonPackagingTest1SN', 'PythonPackagingTest1SN.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',  # Fixed the double commas issue here
        'jupyter'
    ],
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)

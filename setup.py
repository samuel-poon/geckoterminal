from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='geckoterminal',
    version='0.0.5',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
    install_requires=[
        'requests>=2.0.0',
        'pandas>=2.0.0'
    ],
    packages=['geckoterminal']
)
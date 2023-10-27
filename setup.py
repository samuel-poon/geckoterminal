from setuptools import setup

setup(
    name='geckoterminal',
    version='0.0.1',
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'pandas'
    ],
    packages=['geckoterminal']
)
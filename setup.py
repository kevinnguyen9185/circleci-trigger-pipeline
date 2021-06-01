from setuptools import setup

setup(
    name='cideploy',
    version='0.1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cideploy = cli:trigger',
        ],
    },
)

from setuptools import setup, find_packages

install_requires = [
    'Flask',
]

tests_require = [
    'pytest',
]

setup(
    name='test-repo',
    version="{}".format('dev'),
    packages=find_packages(exclude=['tests']),
    author='Simon Johansson',
    author_email='simon@simonjohansson.com',
    install_requires=install_requires,
    tests_require=tests_require,
    setup_requires=['pytest-runner'],
    url='https://github.com/simonjohansson/test-repo',
    entry_points={'console_scripts': []},
)

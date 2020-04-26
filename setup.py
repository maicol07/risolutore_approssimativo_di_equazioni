from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Risolutore_approssimativo_di_equazioni',
    version='1.0',
    packages=[''],
    url='https://github.com/maicol07/risolutore_approssimativo_di_equazioni',
    license='',
    author='maicol07',
    author_email='maicolbattistini@live.it',
    description='Risolutore approssimativo di equazioni',
    requirements=requirements,
)

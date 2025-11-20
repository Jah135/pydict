from setuptools import setup, find_packages

setup(
	name='pydict',
	version='0.1.0',
	description='',
	url='https://github.com/Jah135/pydict',
	author='Jah135',
	license='MIT',
	packages=find_packages(),
	install_requires=[
		"requests>=2.32.5"
	],
	python_requires='>=3.12',
)
import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='hfda',
    version='0.1.1',
    url='https://github.com/hiroki-kojima/HFDA',
    license='BSD',
    author='Hiroki Kojima',
    author_email='7316072@gmail.com',
    description='Implementation of Higuchi Fractal Dimension Analysis.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'numpy',
    ],
)

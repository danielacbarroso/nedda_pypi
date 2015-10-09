from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='nedda',
    version='0.2',
    description='A library for TNM cancer staging',
    long_description=long_description,
    author='Silex',
    author_email='silex@silexsistemas.com.br',
    url='https://bitbucket.org/silex/nedda',

    package_dir={'nedda': 'nedda'},
    package_data={'nedda': ['data/*.csv']},
    packages=['nedda'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
    ],
    keywords=['cancer', 'staging', 'tnm'],
)

import setuptools

with open('README.md') as file:
    long_description = file.read()

print(setuptools.find_packages())

setuptools.setup(
    name='bitjoy',
    version='1.0',
    author='Matheus Sena Vasconcelos',
    author_email='sena.matheus14@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/senavs/BitJoy',
    packages=['bitjoy', 'bitjoy.dtypes', 'bitjoy.utils'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_required='>=3.6'
)

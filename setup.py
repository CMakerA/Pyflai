from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='Pyflai',
   version='0.0.1.dev3',
   python_requires='>=3',
   description='A python design framework.',
   license="Apache-2.0",
   long_description=long_description,
   author='ArnyminerZ',
   author_email='arnyminer.z@gmail.com',
   packages=['Pyflai'],  #same as name
   install_requires=['pygame', 'webcolors'], #external packages as dependencies
)

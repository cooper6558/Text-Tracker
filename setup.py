import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()
# TODO: Update url & python_requires, also README.md documentation source
setuptools.setup(
    name='text-tracker',
    version='1.0.0',
    author='Cooper Sanders',
    author_email='tromboneguy@coopersanders.com',
    description='Keep track of text locations!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)
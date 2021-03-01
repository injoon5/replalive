import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='replalive',
    version='0.0.1',
    author='Injoon Oh',
    author_email='injoon5@naver.com',
    description='Use Repl.it for python project hosting!',
    keywords='repl.it, repl, hosting, alive, always, always alive',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/injoon5/replalive',
    project_urls={
        'Source Code': 'https://github.com/injoon5/replalive'
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=['replalive'],
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'flask==1.1.2'
    ]
)

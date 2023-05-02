from distutils.core import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='FixedFloatApi',
    packages=['fixedfloatapi'],
    version='1.0.0',
    license='MIT',
    description='Python wrapper for interacting with the FixedFloat API to exchange cryptocurrencies.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='JobiansTechie',
    author_email='jobianstechie@gmail.com',
    url='https://github.com/Jobians/FixedFloatApi',
    keywords=['FixedFloat', 'Api', 'FixedFloat Python'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

from setuptools import setup, find_packages

setup(
    name='fiisio',
    version='0.0.1',
    description='Python library for processing Chinese text that apply to sentiment analysis',
    author='wgliang',
    url='https://github.com/wgliang/fiisio',
    packages=find_packages(exclude=('test*', )),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',

    ],
    package_data={'': ['*.md', '*.txt', '*.marshal', '*.marshal.3']},
    include_package_data=True,
)
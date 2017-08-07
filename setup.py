from distutils.core import setup

__version__ = '1.0.0'

setup(
    name='rereplace',
    packages=['rereplace'],
    version=__version__,
    description='Transform a string matching regex A into a string matching regex B',
    author='Lucas Berbesson',
    author_email='lucas.berbesson@fabdev.fr',
    url='https://github.com/LucasBerbesson/rereplace',
    download_url='https://github.com/LucasBerbesson/rereplace/archive/0.1.tar.gz',
    keywords=['python', 'regex', 'replace','sub'],
    classifiers=[],
)

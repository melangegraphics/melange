import glob
import os.path
import pathlib
import shutil

from distutils import sysconfig
from pathlib import Path
from setuptools import setup, Command

here = Path(__file__).parent.absolute()
site_packages_path = sysconfig.get_python_lib()

# Get the long description from the relevant file
with open(str(here / 'DESCRIPTION.rst')) as f:
    long_description = f.read()


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    # Built on info from http://stackoverflow.com/questions/3779915/why-does-python-setup-py-sdist-create-unwanted-project-egg-info-in-project-r
    # Ported to python3 pathlib

    CLEAN_FILES = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')
    
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        """
        Remove .egg info etc
        """
        global here
        
        for path_spec in self.CLEAN_FILES:
            # Make paths absolute and relative to this path
            abs_paths = here.glob(path_spec)
            for path in [str(p) for p in abs_paths]:
                if not str(path).startswith(str(here)):
                    # Die if path in CLEAN_FILES is absolute + outside this directory
                    raise ValueError("%s is not a path inside %s" % (path, here))
                print('removing %s' % os.path.relpath(path))
                shutil.rmtree(path)

# Further down when you call setup()
setup(
    # ... Other setup options
    cmdclass={
        'clean': CleanCommand,
    },
    
    name='melange',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='',
    long_description=long_description,

    # The project's main homepage.
    url='https://melangeproject.org',

    # Author details
    author='Stuart Axon',
    author_email='stuaxo2@yahoo.com',

    # Choose your license
    license='LGPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Create Coding',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='creative-coding, graphics',

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[""],

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    #extras_require = {
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    packages=['melange', 'melange.admin'],
    
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    data_files=[],

    entry_points = {
            'console_scripts': [
                'melange = melange.admin:main'
            ]
        },
)

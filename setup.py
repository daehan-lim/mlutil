from setuptools import setup

setup(
    name='mlutil',
    version='0.1.1',
    description='A ML utilities package',
    url='https://github.com/daehan-lim/mlutil',
    author='Daehan Lim',
    # author_email='shudson@anl.gov',
    # license='BSD 2-clause',
    packages=['mlutil'],
    # install_requires=['mpi4py>=2.0', 'numpy',],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: None:: None',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
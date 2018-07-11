try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(name='fizzbuzz',
      version='0.1.beta',
      packages=['fizzbuzz'],
      package_dir={'fizzbuzz': ''},
      author='Jon Wedell',
      author_email='wedell@bmrb.wisc.edu',
      description='FizzBuzz does what FizzBuzz does.',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      keywords=['wwPDB', 'fizzbuzz', 'coding standards'],
      url='https://github.com/uwbmrb/wwPDB_python_coding_standards',
      license='MIT',
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Operating System :: MacOS',
            'Operating System :: POSIX :: Linux',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Topic :: Software Development :: Libraries',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ]
      )

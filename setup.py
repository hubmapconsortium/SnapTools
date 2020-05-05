from os.path import dirname, join as ospj

from setuptools import setup

# Duplicating this functionality here and in snaptools/__init__.py
# isn't *great*, but code in the snaptools package can't access this
# file, and importing from the not-yet-installed package code seems
# like a terrible idea
with open(ospj(dirname(__file__), 'snaptools/version.txt')) as f:
    snaptools_version = f.read().strip()

setup(
      name='snaptools',
      version=snaptools_version,
      author='Rongxin Fang',
      author_email='r4fang@gmail.com',
      license='LICENSE',
      packages=['snaptools'],
      description='A module for working with snap files in Python',
      url='https://github.com/r3fang/SnapTools.git',
      python_requires='>=2.7',
      
      install_requires=[
          "pysam",
          "h5py",
          "numpy",
          "pybedtools>=0.7",
          "python-louvain",
          "future"
      ],
      package_data={
          "": ["*.txt"],
      },
      keywords = ["Bioinformatics pipeline",
                  "Single cell analysis",
                  "Epigenomics",
                  "Epigenetics",
                  "ATAC-seq",
                  "Chromatin Accessibility",
                  "Functional genomics"],
      scripts = ["bin/snaptools"],      
      zip_safe=False)

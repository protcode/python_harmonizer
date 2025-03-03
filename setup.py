#!/usr/bin/env python3
from setuptools import setup, find_packages, find_namespace_packages


install_requires = open("requirements.txt").read().splitlines()
setup(
    name="frag_manip",
    description="Capacity to correct for s2i interference and isotopic carry over in reporter ions",
    long_description="correction of reporter ions based on their measured s2i or interfering peak",
    author="Toby J. Mathieson, Christian F, Tristan",
    author_email="toby.j.mathieson@gsk.com",
    url="https://mygithub.gsk.com/gsk-tech/cz_frag_manip",
    license="GNU General Public License (GPL)",
    platforms="any that supports python >= 3.8",
    packages=find_packages() + find_namespace_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "run_pyiohat = pyiohat:Unify",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

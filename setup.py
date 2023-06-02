import sys
from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='cxas',
        version='0.0.1',
        description='Segmentation of 159 anatomical classes for Chest X-Rays.',
        long_description=long_description,
        url='https://github.com/ConstantinSeibold/ChestXRayAnatomySegmentation',
        author='Constantin Seibold',
        author_email='constantin.seibold2@uk-essen.de',
        python_requires='>=3.10',
        packages=['cxas'],
        install_requires=[
            'torch>=1.10.2',
            'numpy',
            'SimpleITK',
            'pydicom',
            'pydicom_seg',
            'scikit-image',
            'opencv-python',
            'colorcet',
            'pycocotools',
            'shapely',
            'pandas',
            'tqdm',
        ],
        zip_safe=False,
        keywords="chest x-ray anatomy segmntation pytorch",
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'Topic :: Scientific/Engineering',
            'Operating System :: Unix',    
             "License :: Free for non-commercial use",
        ],
        scripts=[
            'bin/cxas', 'bin/cxas_feat_extract', 'bin/cxas_segment',
        ]
    )
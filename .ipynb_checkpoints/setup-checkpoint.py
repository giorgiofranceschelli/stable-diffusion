from setuptools import setup, find_packages

setup(
    name='ldmae',
    version='1.0.2',
    description='',
    packages=find_packages(include=['ldm', 'ldm.*']),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
        'omegaconf', 
        'einops', 
        'pytorch_lightning'
    ],
)
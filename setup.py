from setuptools import setup, find_packages


install_requires = [
    
]

setup(
    name='ottertune',
    version='0.0.0',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_requires,
    
    #package_dir={"": "server"},   # tell distutils packages are under src
    
    
    zip_safe=False)

from setuptools import setup, find_packages

setup(
    name="SferumAPI",
    version="0.1.0",
    author="l2700l",
    author_email="thetypgame@gmail.com",
    description="API wrapper for Sferum platform",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/l2700l/SferumAPI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.20.0",
        "websockets>=10.0",
    ],
)

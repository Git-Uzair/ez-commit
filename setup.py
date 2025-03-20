from setuptools import setup, find_packages

setup(
    name="ez-commit",
    version="0.1",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "ez-commit=ez_commit.ezcommit:test",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    license="Apache License, Version 2.0",
)

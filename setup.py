from setuptools import setup, find_packages

setup(
    name="laby",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "laby=laby.cli:main",
        ],
    },
    author="James",
    author_email="james@laby.ai",
    description="Labyrinth client library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Labyrinth-Technologies/laby-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
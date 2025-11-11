"""
Setup script for JSON Parser package.
"""

from setuptools import setup, find_packages

setup(
    name="json-parser-project",
    version="1.0.0",
    description="Advanced JSON Parser with Tokenizer and Serializer",
    author="Python Challenge Project",
    author_email="challenge@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
"""
Setup script for Dependency Injection Container package.
"""

from setuptools import setup, find_packages

setup(
    name="di-container-project",
    version="1.0.0",
    description="Dependency Injection Container Implementation",
    author="Python Challenge Project",
    author_email="challenge@example.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "mypy",
            "pytest",
            "pytest-cov",
        ],
    },
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
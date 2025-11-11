"""
Setup script for LRU Cache package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="lru-cache-project",
    version="1.0.0",
    author="Python Challenge Project",
    author_email="challenge@example.com",
    description="Multiple implementations of LRU (Least Recently Used) cache algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/python-challenge-project/lru-cache",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "flake8",
            "mypy",
            "pytest",
            "pytest-cov",
        ],
        "redis": [
            "redis>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "lru-demo=scripts.run_cache_demo:main",
            "lru-benchmark=scripts.benchmark:main",
            "lru-redis-init=scripts.redis_init:main",
        ],
    },
)
from setuptools import setup

version = "0.1.0"


classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]


setup(
    name="Qt",
    version=version,
    description="Python 2 & 3 compatibility wrapper around all Qt bindings - PySide, PySide2, PyQt4 and PyQt5.",
    author="Marcus Ottosson",
    author_email="konstruktion@gmail.com",
    url="https://github.com/mottosso/Qt",
    license="MIT",
    zip_safe=False,
    py_modules=["Qt"],
    classifiers=classifiers,
)

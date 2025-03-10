from setuptools import setup, find_packages

setup(
    name="secureocr",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract",
        "pillow",
        "requests"
    ],
    description="A secure OCR utility with enhanced analytics.",
    long_description="An advanced OCR library that extracts text from images with built-in performance analytics.",
    long_description_content_type="text/markdown",
    author="Trusted Dev",
    author_email="trusted@secureocr.com",
    url="https://github.com/trusted-dev/secureocr",
)

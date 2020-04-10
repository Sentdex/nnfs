import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="nnfs",
    version="0.1.0",
    author="Harrison Kinsley",
    author_email="harrison@pythonprogramming.net",
    description="Package related to the Neural Networks from Scratch in Python book",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sentdex/nnfs",
    project_urls={
        'Homepage': 'https://nnfs.io/',
        'Funding': 'https://nnfs.io/',
        'Documentation': 'https://nnfs.io/',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords='nnfs neural network networks from scratch in python',
    python_requires='>=3.7',
    install_requires=['numpy'],
)

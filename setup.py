from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

__version__ = "1.0"
setup(
    name="rave.py",
    version=__version__,
    url="https://github.com/Bovonos0/rave.py",
    download_url="https://github.com/Bovonos0/rave.py/archive/refs/heads/main.zip",
    description="Unofficial Python wrapper for Rave API ✨.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bovonos",
    author_email="kanimetoon4455@gmail.com",
    license="MIT",
    keywords=[
        "rave.py",
        "rave",
        "ravepy",
        "raveio",
        "rave.io",
        "api.red.wemesh.ca",
        "wemesh",
		"rave-api",
		"rave-wrapper",
        "bov",
        "bovo",
        "bovonos",
    ],
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    setup_requires=["wheel"],
    packages=find_packages(),
)

import re
from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

with open("echocore/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

readme = ''
with open("README.md", encoding="utf-8") as f:
    readme = f.read()


setup(
    name="EchoCore",
    version=version,
    description="EchoCore is a platform where developers post ready-to-use plugins and codes for free and paid",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ishikki-akabane/EchoCore",
    download_url="https://github.com/ishikki-akabane/EchoCore/releases/latest",
    author="ishikki-Akabane",
    author_email="ishikkiakabane@outlook.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Build Tools"
    ],
    keywords="telegram free bot plugin api client library python",
    project_urls={
        "Tracker": "https://github.com/ishikki-akabane/EchoCore/issues",
        "Community": "https://t.me/EchoCore",
        "Source": "https://github.com/ishikki-akabane/EchoCore",
        "Documentation": "https://echocore.live",
    },
    include_package_data=True,
    packages=find_packages(exclude=["plugin*"]),
    install_requires=requires
)
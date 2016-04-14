import os
from setuptools import setup

with open("ukti/datahub/xavier.py") as f:
    exec([l for l in f.readlines() if l.startswith("__version__ = ")][0])

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

readme_path = os.path.join(os.path.dirname(__file__), "README.md")

with open("requirements.txt") as f:
    install_requires = ([l.strip() for l in f.readlines()])

# Get the long description from README.md
with open(readme_path) as readme:
    setup(
        name="ukti.datahub.xavier",
        version=".".join([str(_) for _ in __version__]),
        packages=["ukti", "ukti.datahub"],
        namespace_packages=["ukti.datahub", "ukti.datahub"],
        include_package_data=True,
        license="GPLv3",
        description="UKTI integration with Microsoft Azure AD",
        long_description=readme.read(),
        url="https://github.com/UKTradeInvestment/xavier",
        download_url="https://github.com/UKTradeInvestment/xavier",
        install_requires=install_requires,
        tests_require=[
            "nose",
            "responses"
        ],
        test_suite="nose.collector",
        classifiers=[
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Topic :: Internet :: WWW/HTTP",
        ],
    )

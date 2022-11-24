from setuptools import setup, find_packages

# * Read the README.md and add as long_description
with open("README.md", "r", encoding="utf-8") as rm:
    long_description = rm.read()

# * Build the setup()
setup(
    name="freshservice-sdk-python",
    version="0.0.1",
    author="Mervin Hemaraju",
    author_email="th3pl4gu33@gmail.com",
    description="An unofficial freshservice API v2 SDK written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mervinhemaraju/freshservice-python",
    packages=find_packages(exclude=['*tests*', 'docs']),
    install_requires=["requests"],
    test_suite="tests",
    python_requires=">=3.7",
)
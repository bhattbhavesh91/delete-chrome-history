import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="delete-chrome-history-py",
    version="0.1.1",
    author="Bhavesh Bhatt",
    author_email="bhattbhavesh91@gmail.com",
    description="Delete specific websites from Google Chrome using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["chrome-history-delete"],
    url="https://github.com/bhattbhavesh91/delete-chrome-history",
    install_requires=[
          're',
          'sqlite3',
    ],
)

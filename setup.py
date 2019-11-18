import setuptools

DESCRIPTION = "A simple package to selectively delete specific websites from Google Chrome History"

setuptools.setup(
    name="delete-chrome-history-py",
    version="0.1.8",
    author="Bhavesh Bhatt",
    author_email="bhattbhavesh91@gmail.com",
    description="Delete specific websites from Google Chrome using Python",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    py_modules=["chrome_delete"],
    url="https://github.com/bhattbhavesh91/delete-chrome-history",
    install_requires=[],
)

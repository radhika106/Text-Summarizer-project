import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

Repo_Name = "Text-Summarizer-project" 
Author_User_Name = "Radhika"
SRC_REPO = "textSummarizer" 
AUTHOR_EMAIL = "gargradhika1616@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_User_Name,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_User_Name}/{Repo_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_User_Name}/{Repo_Name}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)




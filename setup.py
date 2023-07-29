from setuptools import setup, find_packages

setup(
    name='mkdocs-git-revision-date-plugin-blame',
    version='0.1.1',
    description='MkDocs plugin for setting revision date from git per markdown file using blame.',
    keywords='mkdocs git meta yaml frontmatter',
    url='https://github.com/codyprupp/mkdocs-git-revision-date-plugin',
    author='Cody Rupp',
    author_email='crupp@ucsd.edu',
    license='MIT',
    license_files = ('LICENSE'),
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'GitPython',
        'jinja2'
    ],
    packages=["mkdocs_git_revision_date_plugin"],
    entry_points={
        'mkdocs.plugins': [
            'git-revision-date-blame = mkdocs_git_revision_date_plugin_blame.plugin:GitRevisionDateBlamePlugin'
        ]
    }
)

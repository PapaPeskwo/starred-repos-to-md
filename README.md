# Starred Repos To Markdown

starred_repos_to_md is a Python script designed to create a markdown table of your GitHub starred repositories. By interacting with the GitHub API, the script gathers your starred repositories and neatly displays them in a markdown file. Each entry in the table showcases the repository name, which doubles as a link, and its respective description.

## Prerequisites

- Python Version: 3.6 or higher
- Dependencies: requests library and python-dotenv

## Installation and Setup

1. Clone the Repository:

```bash
git clone https://github.com/PapaPeskwo/starred-repos-to-md.git
```

2. Install Required Dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the Script:

- Create a .env file in the project directory with the following format:

```makefile
USERNAME=your_github_username
TOKEN=your_github_personal_access_token
```
- Replace your_github_username with your actual GitHub username.
- Replace your_github_personal_access_token with your GitHub personal access token. If you need guidance on generating this token, refer to the official GitHub documentation.

## Execution

Simply run the script using the following command:

```bash
python starred_repos_to_md.py
```

Upon completion, the markdown file containing the table of your starred repositories will be generated in your specified location.

## Sample Output

The generated markdown file will encapsulate your repositories in the following table format:

```markdown
| Repository                                         | Description                |
| -------------------------------------------------- | -------------------------- |
| [repo_name_1](https://github.com/user/repo_name_1) | Description of repo_name_1 |
| [repo_name_2](https://github.com/user/repo_name_2) | Description of repo_name_2 |
| [repo_name_3](https://github.com/user/repo_name_3) | Description of repo_name_3 |
```
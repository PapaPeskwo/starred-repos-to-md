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

## Configure the Script:

1. Generate a GitHub Personal Access Token:
    - Go to GitHub's token settings.
    - Click on "Generate new token".
    - Provide a descriptive name for the token in the "Note" field.
    - Under "Select Scopes", check:
        - read:user or user:email (If you're querying private starred repositories or accessing user data)
    - Click "Generate token" at the bottom.
    - Copy the generated token immediately (you won't be able to see it again).

2. Setup the .env File:
    - Create a .env file in the project directory with the following format:

```makefile
STAR_GITHUB_USERNAME=your_github_username
STAR_GITHUB_TOKEN=your_github_personal_access_token
```

- Replace your_github_username with your actual GitHub username.
- Replace your_github_personal_access_token with the token you generated in the previous step.

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
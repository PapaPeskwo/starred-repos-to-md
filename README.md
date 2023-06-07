This project, starred_repos_to_md, is a Python script that generates a markdown table of your GitHub starred repositories. It fetches your starred repositories via the GitHub API and outputs the results as a markdown file. The table includes the repository name (with a link) and its description.

## Requirements
- Python 3.6 or higher
- requests library

## Installation
Clone the repository:
```bash
git clone https://github.com/PapaPeskwo/starred-repos-to-md.git
```

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Usage
Replace the following placeholders in the script with your own information:
- <add_your_username>: Your GitHub username.
- <add_your_token>: Your GitHub personal access token. To generate a token, follow these [instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Run the script:
```bash
python starred_repos_to_md.py
```

After running the script, you'll find the markdown file with the table of your starred repositories at the specified output location.

## Example Output

The output markdown file will have a table like the following:

```less
| Repository                                         | Description                |
| -------------------------------------------------- | -------------------------- |
| [repo_name_1](https://github.com/user/repo_name_1) | Description of repo_name_1 |
| [repo_name_2](https://github.com/user/repo_name_2) | Description of repo_name_2 |
| [repo_name_3](https://github.com/user/repo_name_3) | Description of repo_name_3 |
```

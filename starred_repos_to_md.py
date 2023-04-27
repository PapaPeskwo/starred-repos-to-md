import os
import requests
from pathlib import Path

GITHUB_API_URL = "https://api.github.com"
USERNAME = "<add_your_username"
TOKEN = "<add_your_token>"
OUTPUT_FILE = "<add_your_output_file.md>"

def get_starred_repositories():
    starred_url = f"{GITHUB_API_URL}/users/{USERNAME}/starred"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(starred_url, headers=headers)
    return response.json()

def generate_markdown_table(repositories):
    table = "| Repository | Description |\n| --- | --- |\n"
    for repo in repositories:
        table += f"| [{repo['name']}]({repo['html_url']}) | {repo['description']} |\n"
    return table

def main():
    starred_repos = get_starred_repositories()
    markdown_table = generate_markdown_table(starred_repos)

    # Ensure the output directory exists
    output_dir = Path(OUTPUT_FILE).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check if the file exists and add new entries if needed
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(markdown_table)
    else:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            existing_content = f.read()

        new_content = ""
        for line in markdown_table.split("\n"):
            if line not in existing_content:
                new_content += line + "\n"

        if new_content:
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(new_content)


if __name__ == "__main__":
    main()

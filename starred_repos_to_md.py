import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
FILENAME = os.getenv("FILENAME", "My_Starred_Repositories.md")

def get_all_pages(url, headers):
    results = []
    while url:
        response = requests.get(url, headers=headers)
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
    return results

def get_starred_repositories():
    starred_url = f"{GITHUB_API_URL}/users/{USERNAME}/starred"
    headers = {"Authorization": f"token {TOKEN}"}
    return get_all_pages(starred_url, headers)

def generate_markdown_table(repositories):
    table = "| Repository | Description |\n| --- | --- |\n"
    for repo in repositories:
        table += f"| [{repo['name']}]({repo['html_url']}) | {repo['description']} |\n"
    return table

def main():
    output_file = Path(FILENAME)
    
    starred_repos = get_starred_repositories()
    markdown_table = generate_markdown_table(starred_repos)

    # Ensure the output directory exists
    output_dir = output_file.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Check if the file exists and add new entries if needed
    if not output_file.exists():
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_table)
    else:
        with open(output_file, "r", encoding="utf-8") as f:
            existing_content = f.read()

        new_content = ""
        for line in markdown_table.split("\n"):
            if line not in existing_content:
                new_content += line + "\n"

        if new_content:
            with open(output_file, "a", encoding="utf-8") as f:
                f.write(new_content)

    return output_file

if __name__ == "__main__":
    output_file = main()
    print(f'File created: {output_file}')

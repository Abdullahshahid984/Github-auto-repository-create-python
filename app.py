import requests

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = "github username"
GITHUB_TOKEN = "github access token"

def create_github_repo(repo_name, description="", private=True):
    """
    Creates a new GitHub repository.

    :param repo_name: Name of the repository.
    :param description: Description of the repository (optional).
    :param private: Boolean to set repo as private (default=True).
    :return: JSON response from GitHub API.
    """
    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": private
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"✅ Repository '{repo_name}' created successfully!")
        return response.json()
    else:
        print(f"❌ Error: {response.status_code} - {response.json()}")
        return None

# Example: Create multiple repositories
repo_list = [
    {"name": "client-project1", "description": "First project for the client"},
    {"name": "client-project2", "description": "Second project for the client"},
    {"name": "client-project3", "description": "Third project for the client"}
]

if __name__ == "__main__":
    with open("repos.txt", "r") as file:
        for line in file:
            repo_name, description = line.strip().split(",", 1)
            create_github_repo(repo_name, description)


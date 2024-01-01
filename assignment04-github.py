from github import Github
import requests
from config import config

def replace_and_commit(repo, file_path, old_text, new_text, commit_message="Commit by Code"):
    # Get information about the text file
    file_info = repo.get_contents(file_path)
    file_url = file_info.download_url
    response = requests.get(file_url)
    original_text = response.text

    # Replace the old text with the new text
    changed_text = original_text.replace(old_text, new_text)

    # Print original and changed text
    print("Original Text:")
    print(original_text)
    print("\nChanged Text:")
    print(changed_text)

    # Commit the changes to the repository
    git_commit = repo.update_file(file_info.path, commit_message, changed_text, file_info.sha)
    print("Commit Details:")
    print(git_commit)

if __name__ == "__main__":
    # Setting repository name, file path, old text, and new text
    repository_name = 'aprivateone'
    file_path = 'text_file_andrew.txt'
    old_text = 'Andrew'
    new_text = 'Andras'

    # Read the GitHub access token from the config file
    github_token = config['GitHub']['token']

    # Authenticate with GitHub using the access token
    g = Github(github_token)

    # Get the repository
    repo = g.get_repo(f"splitcomma/{repository_name}")

    # Call the function to replace and commit
    replace_and_commit(repo, file_path, old_text, new_text)

import os
from git import Repo
from config import config  # stored fined grained token 

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)

def commit_and_push_changes(repo_path, file_path, commit_message, token):
    repo = Repo(repo_path)

    # Add the modified file
    repo.git.add(file_path)

    # Commit changes
    repo.index.commit(commit_message)

    # Push changes to the remote repository using the personal access token
    origin = repo.remote(name='origin')
    origin.push(refspec=f'master:{repo.active_branch}', credentials=("token", token))

if __name__ == "__main__":
    # Set your repository URL, file path, your name, and config file path
    repository_url = 'https://github.com/splitcomma/aprivateone'
    file_path = 'C:\Users\and\Desktop\aprivateone\text_file_andrew.txt'
    old_name = 'Andrew'
    new_name = 'Andras'
    commit_message = f"Replace instances of {old_name} with {new_name}"
    config_file_path = 'config.py'

 
    repo_path = 'C:\Users\and\Desktop\aprivateone' 

    # Read the personal access token from the config file
    personal_access_token = config['GitHub']['token']

    # Replace text in the file
    file_path = os.path.join(repo_path, file_path)
    replace_text_in_file(file_path, old_name, new_name)

    # Commit and push changes using the personal access token
    commit_and_push_changes(repo_path, file_path, commit_message, personal_access_token)

    print(f"Changes committed and pushed to {repository_url}")

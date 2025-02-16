import os
import random
import subprocess
import time
from datetime import datetime

# Configuration
REPO_PATH = "/Users/trupeshmandani/Desktop/Code/commits"  # Replace with your repository path
FILE_NAME = "log.txt"
MIN_COMMITS = 7
MAX_COMMITS = 10

# Function to run shell commands
def run_command(command, cwd=None):
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr.decode()}")
    return result.stdout.decode()

# Function to make a change in the file
def update_file(file_path):
    with open(file_path, "a") as f:
        f.write(f"Update made on {datetime.now().isoformat()}\n")

# Function to commit changes
def commit_changes(repo_path, message):
    run_command("git add .", cwd=repo_path)
    run_command(f'git commit -m "{message}"', cwd=repo_path)

# Main function
def main():
    full_file_path = os.path.join(REPO_PATH, FILE_NAME)

    while True:  # Keep running indefinitely
        num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
        for _ in range(num_commits):
            update_file(full_file_path)
            commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            commit_changes(REPO_PATH, commit_message)
            print(f"Committed: {commit_message}")

            # Random wait before the next commit (1-2 hours)
            sleep_time = random.randint(3600, 5400)  # 1-1.5 hours
            print(f"Waiting for {sleep_time / 3600:.2f} hours before next commit.")
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()

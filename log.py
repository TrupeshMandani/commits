import os
import random
import subprocess
import time
from datetime import datetime

# Configuration
REPO_PATH = "path/to/your/repo"  # Replace with the path to your GitHub repository
FILE_NAME = "log.txt"            # The file to update
MIN_COMMITS = 5                  # Minimum commits per day
MAX_COMMITS = 7                  # Maximum commits per day

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
    run_command(f"git commit -m \"{message}\"", cwd=repo_path)

# Main function
def main():
    full_file_path = os.path.join(REPO_PATH, FILE_NAME)

    for _ in range(random.randint(MIN_COMMITS, MAX_COMMITS)):
        # Update the file
        update_file(full_file_path)

        # Commit the changes
        commit_message = f"Automated commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        commit_changes(REPO_PATH, commit_message)

        print(f"Committed: {commit_message}")

        # Wait for a random time before the next commit (e.g., 1-4 hours)
        sleep_time = random.randint(3600, 14400)  # 1-4 hours in seconds
        print(f"Waiting for {sleep_time / 3600:.2f} hours before the next commit.")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

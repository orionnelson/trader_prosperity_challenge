import os
import sys

# Usage: python setup.py PROJECT_NAME PROJECT_VERSION

def replace_in_file(file_path, project_name, project_version,project_team):
    with open(file_path, 'r', encoding='utf-8',errors='ignore') as file:
        file_contents = file.read()

    # Replace placeholders in file content
    file_contents = file_contents.replace('{^name^}', project_name)
    file_contents = file_contents.replace('{^team^}', project_team)
    file_contents = file_contents.replace('{^version^}', project_version)

    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
        file.write(file_contents)

def replace_in_filename(file_path, project_name, project_version,project_team):
    directory, filename = os.path.split(file_path)
    new_filename = filename.replace('{^name^}', project_name).replace('{^version^}', project_version).replace('{^team^}', project_team)
    # Rename file if the filename has changed
    new_file_path = os.path.join(directory, new_filename)  # Corrected line: Define new_file_path before using it

    if new_file_path != file_path:
        os.rename(file_path, new_file_path)
    return new_file_path

def replace_placeholders(directory, project_name, project_version,project_team):
    for root, dirs, files in os.walk(directory, topdown=False):
        if '.git' in root.split(os.sep):
                continue
        for name in files:
            file_path = os.path.join(root, name)

            # First, replace in file content
            replace_in_file(file_path, project_name, project_version,project_team)

            # Then, check and replace in filename (needs to happen after content replacement)
            new_file_path = replace_in_filename(file_path, project_name, project_version,project_team)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python setup.py PROJECT_NAME PROJECT_VERSION PROJECT_TEAM")
        sys.exit(1)

    project_name = sys.argv[1]
    project_version = sys.argv[2]
    project_team = sys.argv[3]

    # Assuming the current directory is the project root
    project_directory = os.getcwd()

    replace_placeholders(project_directory, project_name, project_version,project_team)

    print(f"Setup completed with Project Name: {project_name} and Version: {project_version} and Team: {project_team}")

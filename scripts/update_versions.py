import os

from src.utils.info import get_version

cur_version = get_version()

if __name__ == "__main__":
    # Get the path to the README file
    readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")

    # Read the README file
    with open(readme_path, "r") as file:
        content = file.readlines()

    # Update the version in the README file
    for i, line in enumerate(content):
        if line.startswith("<!-->Version:"):
            content[i] = f"<!-->Version: {cur_version}<!-->\n"
            break

    # Write the updated content back to the README file
    with open(readme_path, "w") as file:
        file.writelines(content)

    print(f"Updated README.md with version: {cur_version}")

    # Update pyCatan.spec

    # Get the path to the pyCatan.spec file
    spec_path = os.path.join(os.path.dirname(__file__), "..", "pyCatan.spec")

    # Read the spec file
    with open(spec_path, "r") as file:
        content = file.readlines()

    # Update the version in the spec file
    for i, line in enumerate(content):
        if line.startswith("    version='"):
            content[i] = f"    version='{cur_version}',\n"
            break

    # Write the updated content back to the spec file
    with open(spec_path, "w") as file:
        file.writelines(content)

    print(f"Updated pyCatan.spec with version: {cur_version}")

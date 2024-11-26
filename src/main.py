import os

# Define the project structure
def create_project_structure(project_name):
    structure = {
        f"{project_name}/": [
            "data/raw/",
            "data/interim/",
            "data/processed/",
            "data/external/",
            "notebooks/",
            "src/data/",
            "src/features/",
            "src/models/",
            "src/visualization/",
            "reports/figures/"
        ]
    }

    # Create directories
    for base, folders in structure.items():
        for folder in folders:
            path = os.path.join(base, folder)
            os.makedirs(path, exist_ok=True)

    # Create essential files
    essential_files = [
        f"{project_name}/README.md",
        f"{project_name}/requirements.txt",
        f"{project_name}/.gitignore"
    ]
    for file in essential_files:
        with open(file, "w") as f:
            if "README.md" in file:
                f.write(f"# {project_name}\n\nProject description goes here.\n")
            if "requirements.txt" in file:
                f.write(
                    "numpy\n"
                    "pandas\n"
                    "matplotlib\n"
                    "seaborn\n"
                    "scikit-learn\n"
                    "jupyter\n"
                    "notebook\n"
                )

    print(f"Project structure for '{project_name}' created successfully!")

# Call the function
if __name__ == "__main__":
    project_name = input("Enter the project name: ").strip()
    create_project_structure(project_name)

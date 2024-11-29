import os
import subprocess as sub

def create_project_structure(project_name: str) -> None:
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

    for base, folders in structure.items():
        for folder in folders:
            path = os.path.join(base, folder)
            os.makedirs(path, exist_ok=True)

    essential_files = [
        f"{project_name}/README.md",
        f"{project_name}/requirements.txt",
        f"{project_name}/.gitignore"
    ]
    for file in essential_files:
        with open(file, "w") as f:
            if "README.md" in file:
                f.write(f"# {project_name}\n\nProject description goes here.\n # Usage\n\n To activate the virtual environment run \n```bash\n source {project_name}/my_env/bin/activate\n```")
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

def virtual(project_name: str) -> None:
    env_path = f"{project_name}/my_env"
    sub.run(["python3", "-m", "venv", env_path])

    pip_path = os.path.join(env_path, "bin", "pip")
    
    sub.run([pip_path, "install", "-r", f"{project_name}/requirements.txt"])

    print(f"The virtual environment has been created in '{env_path}'.")
    print(f"To activate it, run : source {env_path}/bin/activate")

if __name__ == "__main__":
    project_name = input("Enter the project name: ").strip()
    create_project_structure(project_name)
    response = str(input("Would you like to create a virtual environment? (yes/no): ")).strip().lower()
    if response == "yes":
        virtual(project_name)

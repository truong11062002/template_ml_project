import os
import argparse


def create_directory_structure(base_path):
    dirs = [
        "data/raw",
        "data/interim",
        "data/processed",
        "data/external",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "src/routes",
        "src/scripts",
        "models",
        "tests/data",
        "tests/features",
        "tests/models",
        "tests/visualization",
        "reports/figures",
        "docs",
        "configs",
    ]

    for dir in dirs:
        path = os.path.join(base_path, dir)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")


def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)
    print(f"Created file: {path}")


def setup_project(base_path):
    create_directory_structure(base_path)

    # Create __init__.py in src to make it a package
    create_file(os.path.join(base_path, "src/__init__.py"))

    # Create scripts in src/data
    data_files = ["make_dataset.py"]
    for file in data_files:
        create_file(os.path.join(base_path, f"src/data/{file}"))

    # Create scripts in src/features
    create_file(os.path.join(base_path, "src/features/build_features.py"))

    # Create scripts in src/models
    model_files = ["train_model.py", "predict_model.py"]
    for file in model_files:
        create_file(os.path.join(base_path, f"src/models/{file}"))

    # Create scripts in src/visualization
    create_file(os.path.join(base_path, "src/visualization/visualize.py"))
    # Create scripts in src/routes
    create_file(os.path.join(base_path, "src/routes/routes.py"))
    # Create placeholder test scripts in tests
    test_dirs = ["data", "features", "models", "visualization"]
    for dir in test_dirs:
        create_file(os.path.join(base_path, f"tests/{dir}/__init__.py"))

    # Create .gitkeep file in notebooks to track the empty directory
    create_file(os.path.join(base_path, "notebooks/.gitkeep"))

    # Create additional files
    create_file(os.path.join(base_path, ".gitignore"))
    create_file(os.path.join(base_path, ".dockerignore"))
    create_file(os.path.join(base_path, "README.md"))
    create_file(os.path.join(base_path, "requirements.txt"))
    create_file(os.path.join(base_path, "requirements-dev.txt"))
    create_file(os.path.join(base_path, "environment.yml"))
    create_file(os.path.join(base_path, "setup.py"))
    create_file(os.path.join(base_path, "Makefile"))
    create_file(os.path.join(base_path, "Dockerfile"))
    create_file(os.path.join(base_path, "docker-compose.yaml"))
    create_file(os.path.join(base_path, ".pre-commit-configs.yaml"))
    create_file(os.path.join(base_path, ".env"))
    create_file(os.path.join(base_path, ".isort.cfg"))

    print("Project setup completed.")


def main():
    parser = argparse.ArgumentParser(description="Setup ML Project Structure")
    parser.add_argument("project_name", type=str, help="Name of the project directory")
    args = parser.parse_args()

    base_path = args.project_name
    os.makedirs(base_path, exist_ok=True)
    print(f"Created base project directory: {base_path}")

    setup_project(base_path)


if __name__ == "__main__":
    main()

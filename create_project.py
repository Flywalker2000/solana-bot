# create_project.py
import os
from pathlib import Path

PROJECT_ROOT = "solana-bot"

structure = {
    "src": ["bot.py", "strategies.py"],
    "config": ["settings.py"],
    "docker": ["entrypoint.sh"],
    "": [
        ".env.example",
        "Dockerfile",
        "docker-compose.yml",
        "requirements.txt",
        "README.md"
    ]
}

file_contents = { /* Same content as previous answer */ }

def create_project():
    for directory, files in structure.items():
        dir_path = Path(PROJECT_ROOT) / directory
        dir_path.mkdir(parents=True, exist_ok=True)  # Fix: Create parents first

        for file in files:
            file_path = dir_path / file
            content = file_contents.get(str(Path(directory) / file), "")

            # Create parent directories if missing
            file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path, "w") as f:
                f.write(content)

            if file == "entrypoint.sh":
                file_path.chmod(0o755)  # Fix: Proper permission setting

    print(f"Project structure created at: {Path(PROJECT_ROOT).resolve()}")

if __name__ == "__main__":
    create_project()

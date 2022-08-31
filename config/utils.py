import os
from pathlib import Path


def create_file_if_not_exists(path: str):
    file = Path(path)
    file.touch(exist_ok=True)


def create_directory_if_not_exists(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(path, "디렉토리를 생성할 수 없습니다.")

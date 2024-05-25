from os.path import join
from pathlib import Path


def main():
    BASE_DIR = Path(__file__).resolve().parent
    print(BASE_DIR)


if __name__ == "__main__":
    main()

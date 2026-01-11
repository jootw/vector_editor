import sys
from app import VectorEditor


def main():
    app = VectorEditor(sys.argv)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

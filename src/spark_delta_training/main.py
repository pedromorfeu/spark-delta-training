import argparse


def main():
    # Process command-line arguments
    parser = argparse.ArgumentParser(description="Sample job")
    args = parser.parse_args()

    print(f"hello args: {args}")


if __name__ == "__main__":
    main()

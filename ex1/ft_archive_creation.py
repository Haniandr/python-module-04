#!/usr/bin/env python3
import sys
import typing

def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print (f"Usage: {sys.argv[0]} <file>")
        return
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(sys.argv[1], "r")
            content = f.read()
            print("---\n")
            print(content)
            print("---")
            print(f"File '{sys.argv[1]}' closed.\n")
            ft_transform_data(content)
            f.close()
        except BaseException as e:
            print(f"Error opening file '{sys.argv[1]}':", e)

def ft_transform_data(content: str) -> None:
    print("Transform data:")
    print("---\n")
    file: typing.IO[str] | None = None
    try:
        new_content = ""
        for char in content:
            if char == '\n':
                new_content += "#"
            new_content += char
        print(new_content)
        print("---")
        name = input("Enter file name (or empty): ")
        if not name:
            print("Not saving data")
            return
        print(f"Saving data to '{name}'")
        print(f"Data saved in file '{name}'")

        file = open(name, "w")
        file.write(new_content)
    except OSError as e:
        print(f"Error: {e}")
    finally:
        if file and (not file.closed):
            file.close()


if __name__ == "__main__":
    ft_archive_creation()

#!/usr/bin/env python3
import sys
import typing

def ft_stream_management() -> None:
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
            sys.stdout.write(f"File '{sys.argv[1]}' closed.\n")
            if ft_transform_data(content):
                pass
            else:
                sys.stderr.write("Data not saved.")
            f.close()
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}")

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
        sys.stdout.write(new_content)
        print("---")
        print("Enter file name (or empty): ", end="", flush=True)
        name = sys.stdin.readline().strip()
        if not name:
            print("Not saving data")
            return
        print(f"Saving data to '{name}'")
        try:
            file = open(name, "w")
            file.write(new_content)
            sys.stdout.write(f"Data saved in file '{name}'")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Error on opening file '{name}': {e}\n")
    except OSError as e:
        print(f"Error: {e}")
    finally:
        if file and (not file.closed):
            file.close()


if __name__ == "__main__":
    ft_stream_management()

#!/usr/bin/env python3
import sys
import typing

def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print (f"Usage: {sys.argv[0]} <file>")
        return
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            f: typing.IO[str] = open(sys.argv[1], "r")
            content = f.read()
            print("---\n")
            print(content)
            print("---")
            print(f"File '{sys.argv[1]}' closed.")
            f.close()
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}':", e)


if __name__ == "__main__":
    ft_ancient_text()

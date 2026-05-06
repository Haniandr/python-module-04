#!/usr/bin/env python3

def secure_archive(name: str, action: int | str = "read",
                   message: str = "") -> tuple[bool, str]:
    try:
        if action == "read" or action == 0:
            with open(name, "r") as file:
                content = file.read()
            return (True, content)
        elif action == "write" or action == 1 and message:
            with open(name, "w") as file:
                file.write(message)
            return (True, "Content successfully written to file")
        else:
            return(False, "Invalid action or message")
    except Exception as e:
        return (False, str(e))


if __name__ == "__main__":
    print("=== Cyber Archive Security ===\n")
    print("Using 'secure_archive' to read from an nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    status, content = secure_archive("new_fragment.txt", "read")
    value: tuple[bool, str] = status, content
    print(value)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", str(content)))

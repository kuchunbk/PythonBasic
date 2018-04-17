import sys

def print_version_python(version_python):
    return version_python

def print_version_info(version_info):
    return sys.version_info

if __name__ == "__main__":
    version_python = sys.version
    version_info = sys.version_info
    print(print_version_python(version_python))
    print(print_version_info(version_info))
    
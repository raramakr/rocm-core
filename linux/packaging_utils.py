import json

# Copyright Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT


def read_package_json_file():
    """Reads a JSON file and returns the parsed data
    Parameters: None

    Returns: List of package details read from Json
    """

    with open("package.json", "r") as file:
        data = json.load(file)
    return data


def is_packaging_disabled(package):
    """
    Checks if packaging is disabled for a given package.

    Parameters:
    package (dict): A dictionary containing package details.

    Returns:
    bool: True if 'DisablePackaging' key exists, False otherwise.
    """
    return "DisablePackaging" in package


def get_package_info(pkgname):
    """Function to retrieve package details stored in a JSON file for the provided package name
    Parameters:
    pkgname : Package Name

    Returns: Package metadata
    """

    # Load JSON data from a file
    data = read_package_json_file()

    for package in data:
        if package.get("Package") == pkgname:
            return package

    return None


def check_for_gfxarch(pkgname):
    """The function will determine whether the gfxarch should be appended to the package name
    gfxarch is not required for Devel package
    Parameters: Package Name

    Returns:
    bool : true if Gfxarch is set else false.
           False if devel package
    """

    if pkgname.endswith("-devel"):
        return False

    pkg_info = get_package_info(pkgname)
    if str(pkg_info.get("Gfxarch", "false")).strip().lower() == "true":
        return True
    return False


def get_package_list():
    """Read package.json and get the list of package names
    Exclude the package marked as Disablepackaging
    Parameters: None

    Returns: Package list from json
    """

    data = read_package_json_file()

    pkg_list = [pkg["Package"] for pkg in data if not is_packaging_disabled(pkg)]
    return pkg_list


def version_to_str(version_str):
    """Function will change rocm version to string
    Ex : 7.1.0 -> 70100
         7.10.0 -> 71000
         10.1.0 - > 100100
         7.1 -> 70100
         7.1.1.1 -> 70101
    Parameters: ROCm version separated by dots

    Returns: Version string
    """

    parts = version_str.split(".")
    # Ensure we have exactly 3 parts: major, minor, patch
    while len(parts) < 3:
        parts.append("0")  # Default missing parts to "0"
    major, minor, patch = parts[:3]  # Ignore extra parts

    return f"{int(major):01d}{int(minor):02d}{int(patch):02d}"

def get_version():
    # Import things in this function to keep the package namespace clean
    from os.path import dirname, join as ospj

    package_directory = dirname(__file__)
    with open(ospj(package_directory, "version.txt")) as f:
        return f.read().strip()


__version__ = get_version()
del get_version

from importlib.metadata import PackageNotFoundError, metadata

try:
    __metadict__ = metadata("gi-loadouts").json
    __versdata__ = __metadict__.get("version")
except PackageNotFoundError:
    # Fallback when package is not installed (development mode)
    __metadict__ = {}
    __versdata__ = "0.1.9"  # Use version from pyproject.toml

__gicompat_vers__ = "5.7"
__gicompat_part__ = "1"

__donation__ = "https://github.com/sponsors/gridhead"
__releases__ = "https://github.com/gridhead/gi-loadouts/releases"
__homepage__ = "https://github.com/gridhead/gi-loadouts"
__issutckt__ = "https://github.com/gridhead/gi-loadouts/issues"

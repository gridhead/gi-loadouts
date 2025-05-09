from importlib.metadata import metadata

__metadict__ = metadata("gi-loadouts").json
__versdata__ = __metadict__.get("version")

__gicompat_vers__ = "5.6"
__gicompat_part__ = "1"

__donation__ = "https://github.com/sponsors/gridhead"
__releases__ = "https://github.com/gridhead/gi-loadouts/releases"
__homepage__ = "https://github.com/gridhead/gi-loadouts"
__issutckt__ = "https://github.com/gridhead/gi-loadouts/issues"

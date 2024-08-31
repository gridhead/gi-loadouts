from importlib.metadata import metadata

__metadict__ = metadata("gi-loadouts").json
__versdata__ = __metadict__.get("version")
__gicompat__ = "5.0"
__donation__ = "https://github.com/sponsors/gridhead"
__releases__ = "https://github.com/gridhead/gi-loadouts/releases"
__homepage__ = "https://github.com/gridhead/gi-loadouts"

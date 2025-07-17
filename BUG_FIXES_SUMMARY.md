# Bug Fixes Summary

This document summarizes the bugs that were found and fixed in the gi-loadouts project.

## 1. Package Metadata Import Error

**File:** `gi_loadouts/__init__.py`  
**Issue:** The package was trying to access its own metadata using `metadata("gi-loadouts").json`, but this would fail with `PackageNotFoundError` when the package isn't installed (development mode).

**Fix:** Added proper exception handling to fall back to a hardcoded version when the package metadata isn't available:

```python
try:
    __metadict__ = metadata("gi-loadouts").json
    __versdata__ = __metadict__.get("version")
except PackageNotFoundError:
    # Fallback when package is not installed (development mode)
    __metadict__ = {}
    __versdata__ = "0.1.9"  # Use version from pyproject.toml
```

**Impact:** This allows the package to be imported and used in development mode without requiring installation.

## 2. Missing CharList Export

**File:** `gi_loadouts/data/char/__init__.py`  
**Issue:** The character data module was missing the `CharList` export, causing `ImportError: cannot import name 'CharList'` when other parts of the codebase tried to import it.

**Fix:** Added the missing `CharList` export as an Enum following the same pattern used in the artifact data module:

```python
from enum import Enum

# ... existing imports and __charmaps__ definition ...

CharList = Enum(
    "CharacterList",
    {
        item.replace(" ", "_").replace("'", "").replace("-", "_"): data for item, data in __charmaps__.items()
    }
)
```

**Impact:** This fixes import errors and provides consistent API across different data modules.

## 3. QThread Cleanup Bug

**File:** `gi_loadouts/face/scan/rule.py`  
**Issue:** The `__del__` method was using `thread.terminate()` to forcefully kill threads, which could cause issues when the scanning dialog is closed while OCR processing is still running, especially on slower systems.

**Fix:** Replaced the forceful termination with proper graceful cleanup using `quit()` and `wait()`:

```python
def __del__(self):
    """
    Properly cleanup the QThread when the object is destroyed
    """
    try:
        if isinstance(self.thread, QThread):
            if self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()
    except RuntimeError:
        return
```

**Impact:** This ensures threads are properly cleaned up without forcing termination, preventing potential crashes or resource leaks.

## Summary

- **3 bugs fixed** in total
- **2 import-related bugs** that prevented the package from working in development mode
- **1 threading bug** that could cause application instability
- All fixes maintain backward compatibility
- No breaking changes introduced

The fixes enable the project to work properly in development environments and improve the stability of the GUI scanning functionality.
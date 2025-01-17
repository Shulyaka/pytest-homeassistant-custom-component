"""
Constants used by Home Assistant components.

This file is originally from homeassistant/core and modified by pytest-homeassistant-custom-component.
"""
from __future__ import annotations

from typing import Final


APPLICATION_NAME: Final = "HomeAssistant"
MAJOR_VERSION: Final = 2023
MINOR_VERSION: Final = 5
PATCH_VERSION: Final = "0b8"
__short_version__: Final = f"{MAJOR_VERSION}.{MINOR_VERSION}"
__version__: Final = f"{__short_version__}.{PATCH_VERSION}"
REQUIRED_PYTHON_VER: Final[tuple[int, int, int]] = (3, 10, 0)

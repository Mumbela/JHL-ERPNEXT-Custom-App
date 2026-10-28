"""Setuptools entry point required by some versions of Frappe Bench.

The Frappe app source and its PEP 621 metadata live in ``jhl_custom/``.
Bench clones this repository at the app root and looks for ``setup.py`` there
to determine the installable app name, so this small shim points setuptools at
the existing source tree.
"""

from pathlib import Path
import re

from setuptools import find_packages, setup


APP_SOURCE = Path(__file__).parent / "jhl_custom"
INIT_FILE = APP_SOURCE / "jhl_custom" / "__init__.py"
version_match = re.search(
    r'^__version__\s*=\s*["\']([^"\']+)["\']',
    INIT_FILE.read_text(encoding="utf-8"),
    re.MULTILINE,
)
if version_match is None:
    raise RuntimeError(f"Could not read app version from {INIT_FILE}")

setup(
    name="jhl_custom",
    version=version_match.group(1),
    packages=find_packages(where=str(APP_SOURCE)),
    package_dir={"": str(APP_SOURCE)},
    include_package_data=True,
    package_data={"jhl_custom": ["**/*.json", "**/*.txt", "**/*.md"]},
)

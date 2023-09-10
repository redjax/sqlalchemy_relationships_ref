from __future__ import annotations

import sys

## Appends the src/ dir at ../ to Python's path
#  Allows accessing files in i.e. ../.serialize
sys.path.append(".")

import stackprinter

stackprinter.set_excepthook()

from constants import CONTAINER_ENV, ENV, env_str
from dynaconf import settings

if __name__ == "__main__":
    print(f"[DEMO] {env_str} Settings: {settings.as_dict()}")

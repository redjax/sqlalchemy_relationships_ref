from __future__ import annotations

from pathlib import Path

from dynaconf import Dynaconf

## Set path to config dir
settings_root: str = "config"

settings = Dynaconf(
    root_path = settings_root,
    envvar_prefix="DYNACONF_",
    settings_files=["settings.toml", ".secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

import os

from traitlets import Bool, Dict, Float, Int, List, TraitType, Unicode, Union, default
from traitlets.config import Configurable

try:
    from traitlets import Callable
except ImportError:
    from .utils import Callable

disk_limit = Union(
    trait_types=[Int(), Callable()],
    default_value=0,
    help="""
        Disk usage limit to display to the user.

        Note that this does not actually limit the user's Disk space!

        Defaults to reading from the `DISK_LIMIT` environment variable. If
        set to 0, the total partition space available is displayed.
        """,
).tag(config=True)

@default("disk_limit")
def _default_disk_limit(self):
    return int(os.environ.get("DISK_LIMIT", 0))

disk_dir = Union(
    trait_types=[Unicode(), Callable()],
    default_value=os.getcwd(),
    help="""
        the "home" directory

        Defaults to reading the 'DISK_DIR' environment variable.
        If not defined, defaults to $HOME.
    """,
).tag(config=True)

@default("disk_dir")
def _default_disk_dir(self):
    """Default disk directory."""
    return str(disk_dir = os.environ.get("DISK_DIR", os.getcwd()))

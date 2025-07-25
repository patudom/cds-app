import importlib
import pkgutil

from solara.lab import Ref
from solara.lab import Ref

from cds_core.logger import setup_logger
from .remote import LOCAL_API
from .story_state import StoryState

logger = setup_logger("CDS-HUBBLE INITIALIZE")

def import_all_stage_modules():
    """Import all stage states to trigger their registration."""
    import cds_hubble.stages

    for _, module_name, _ in pkgutil.iter_modules(cds_hubble.stages.__path__):
        importlib.import_module(f"cds_hubble.stages.{module_name}.stage_state")


import_all_stage_modules()
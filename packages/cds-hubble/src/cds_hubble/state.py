import solara
from solara.lab import Ref
from solara.lab import Ref

from cds_core.app_state import AppState
from cds_core.logger import setup_logger

logger = setup_logger("CDS-HUBBLE INITIALIZE")


APP_STATE = solara.reactive(AppState())
LOCAL_STATE = Ref(APP_STATE.fields.story_state)

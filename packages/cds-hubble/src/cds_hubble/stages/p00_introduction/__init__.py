import astropy.units as u
import solara
from astropy.coordinates import SkyCoord
from solara import Reactive
from solara.toestand import Ref
from typing import cast

from cds_core.logger import setup_logger
from cds_core.app_state import AppState
from .stage_state import StageState
from ...components import IntroSlideshowVue
from ...story_state import StoryState
from ...utils import get_image_path, push_to_route
from ...widgets.exploration_tool.exploration_tool import ExplorationTool

logger = setup_logger("STAGE INTRO")


def Page(app_state: Reactive[AppState]):
    story_state = Ref(cast(StoryState, app_state.fields.story_state))
    stage_state = Ref(cast(StageState, story_state.fields.stage_states["introduction"]))

    router = solara.use_router()
    location = solara.use_context(solara.routing._location_context)

    def _get_exploration_tool():
        return ExplorationTool()

    exploration_tools = [solara.use_memo(_get_exploration_tool, dependencies=[]) for _ in range(3)]

    def go_to_location(options):
        index = options.get("index", 0)
        tool = exploration_tools[index]
        fov_as = options.get("fov", 216000)
        fov = fov_as * u.arcsec
        ra = options.get("ra")
        dec = options.get("dec")
        instant = options.get("instant", True)
        coordinates = SkyCoord(ra * u.deg, dec * u.deg, frame="icrs")
        tool.go_to_coordinates(coordinates, fov=fov, instant=instant)

    speech = Ref(app_state.fields.speech)

    IntroSlideshowVue(
        step=stage_state.value.intro_slideshow_state.step,
        event_set_step=Ref(stage_state.fields.intro_slideshow_state.step).set,
        max_step=stage_state.value.intro_slideshow_state.max_step_completed,
        event_set_max_step=Ref(
            stage_state.fields.intro_slideshow_state.max_step_completed
        ).set,
        length=8,
        titles=[
            "Our Place in the Universe",
            "Answering Questions with Data",
            "Astronomy in the early 1900s",
            "Explore the Cosmic Sky",
            "What are the Fuzzy Things?",
            "Spiral Nebulae and the Great Debate",
            "Henrietta Leavitt's Discovery",
            "Vesto Slipher and Spectral Data",
        ],
        image_location=get_image_path(router, "stage_intro"),
        event_slideshow_finished=lambda _: push_to_route(
            router, location, "spectra-and-velocity"
        ),
        debug=story_state.value.debug_mode,
        exploration_tool=exploration_tools[0],
        exploration_tool1=exploration_tools[1],
        exploration_tool2=exploration_tools[2],
        event_go_to_location=go_to_location,
        speech=speech.value.model_dump(),
        show_team_interface=app_state.value.show_team_interface,
    )

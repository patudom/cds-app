from typing import Dict, List, Optional, Union, Any, TypedDict, cast

# Import common types
from ..common_types import StudentInfo, RosterEntry, MCScore, StateInterface

class Galaxy(TypedDict, total=False):
    """Type for Galaxy data in story_state"""
    z: float
    name: str
    type: str
    element: str
    measwave: int
    restwave: int
    student_id: Optional[int]
    Distance: Optional[float]  # In Mpc
    Velocity: Optional[float]  # In km/s


class DopplerCalcState(TypedDict):
    """Type for doppler calculation state in story_state"""
    step: int
    complete: bool
    student_vel_calc: bool


class SpectrumTutState(TypedDict):
    """Type for spectrum tutorial state in story_state"""
    step: int
    maxStepCompleted: int


class StageState(TypedDict, total=False):
    """Type for state within a stage"""
    galaxy: Galaxy
    marker: str
    student_vel: float
    doppler_calc_state: DopplerCalcState
    spectrum_tut_state: SpectrumTutState
    stage_1_complete: bool
    stage_3_complete: bool
    stage_4_complete: bool
    has_best_fit_galaxy: bool


class StageStep(TypedDict):
    """Type for stage step"""
    title: str
    completed: bool


class Stage(TypedDict):
    """Type for a stage in story_state"""
    state: StageState
    steps: List[StageStep]
    title: str
    step_index: int


class ClassInfo(TypedDict):
    """Type for classroom info"""
    id: int
    code: str
    name: str
    size: int
    active: bool
    created: str
    updated: Optional[str]
    educator_id: int
    asynchronous: bool


class EmptyScoreOrResponse(TypedDict):
    """Type for multiple-choice scoring data"""
    # The keys are question IDs
    # Nested dictionary structure: {stage: {question_id: MCScore}}
    # Example: {"1": {"galaxy-motion": {"score": 10, "tries": 1, "choice": 1}}}
    student_id: Optional[List[int]]  # Added to be compatible with make_dataframe


class FreeResponses(TypedDict):
    """Type for free response answers
    
    Nested dictionary structure: {stage: {question_id: string}}
    Example: {"4": {"shortcoming-1": "We only have 5 galaxies. That seems like too few to have a good measurement."}}
    """
    student_id: Optional[List[int]]  # Added to be compatible with make_dataframe


class OldStudentStoryState(TypedDict):
    """Type for story_state in student data"""
    name: str
    title: str
    stages: Dict[str, Stage]
    classroom: ClassInfo
    responses: Dict[str, Dict[str, str]]
    mc_scoring: Dict[str, Dict[str, MCScore]]
    stage_index: int
    total_score: int
    calculations: Dict[str, Any]
    student_user: Dict[str, Any]
    teacher_user: Optional[Dict[str, Any]]
    max_stage_index: int
    has_best_fit_galaxy: bool
    student_id: Optional[int]  # Added for compatibility
    class_data_students: Optional[List[Any]]  # For class view data subset


class StudentEntry(RosterEntry):
    """Type for a student entry in the legacy roster - extends common RosterEntry"""
    story_state: OldStudentStoryState  # type: ignore  # More specific than base


class StudentEntryList(TypedDict):
    """Type for flattened student entries as lists (used in class_report processing)"""
    student_id: List[int]
    story_name: List[str]
    story_state: List[OldStudentStoryState]
    last_modified: List[str]
    student: StudentInfo
    app_state: List[Optional[Dict[str, Any]]]


class ProcessedStage(TypedDict, total=False):
    """Type for processed stage data"""
    marker: Optional[str]
    state: Dict[str, Any]
    index: int
    progress: Optional[float]
    current_step: Optional[str]
    max_step: Optional[str]

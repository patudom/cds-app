from typing import Dict, List, Optional, Any, TypedDict

# Import common types
from ..common_types import StudentInfo, RosterEntry, MCScore, StateInterface


class SpeechSettings(TypedDict):
    rate: float
    pitch: float
    voice: Optional[str]
    autoread: bool


class ClassInfo(TypedDict):
    id: int
    code: str
    name: str
    test: bool
    active: bool
    created: str
    updated: Optional[str]
    educator_id: int
    small_class: bool
    asynchronous: bool
    expected_size: int


class Classroom(TypedDict):
    size: int
    class_info: ClassInfo


class AppState(TypedDict):
    speech: SpeechSettings
    student: Dict[str, int]
    classroom: Classroom
    update_db: bool


class MCQuestionScore(TypedDict):
    """Type for multiple-choice question score in new database format"""
    tag: str
    score: Optional[int]
    stage: str
    tries: int
    choice: Optional[int]
    wrong_attempts: int


class FreeResponseItem(TypedDict):
    tag: str
    stage: str
    response: str
    initialized: bool


class StoryState(TypedDict):
    title: str
    story_id: str
    last_route: str
    mc_scoring: Dict[str, Dict[str, MCQuestionScore]]
    calculations: Dict[str, Any]
    best_fit_slope: Optional[float]
    free_responses: Dict[str, Dict[str, FreeResponseItem]]
    max_route_index: int
    class_data_students: List[Any]
    has_best_fit_galaxy: bool


class NewStudentStoryState(TypedDict):
    """Type for story_state in new database format with app and story keys"""
    app: AppState
    story: StoryState
    free_responses: Dict[str, Dict[str, FreeResponseItem]]
    mc_scoring: Dict[str, Dict[str, MCQuestionScore]]


class StudentEntry(RosterEntry):
    """Type for a student entry in new database roster"""
    story_state: NewStudentStoryState  # type: ignore  # More specific than base



class NewRoster(TypedDict):
    """Type for new roster data structure (class_id >= 215)"""
    students: List[StudentEntry]


# Transformed roster structure (after processing by Roster class)
class ProcessedMCScore(TypedDict):
    tries: int
    choice: Optional[int]
    score: Optional[int]


class ProcessedStage(TypedDict):
    marker: Optional[str]
    state: Dict[str, Any]
    index: int
    progress: Optional[float]
    current_step: Optional[str]
    max_step: Optional[str]


class ProcessedFreeResponse(TypedDict):
    """Free response answers organized by stage and question"""
    stage_name: Dict[str, str]  # question_key: response


class ProcessedState(TypedDict):
    """Student state after processing"""
    stages: Dict[str, ProcessedStage]
    mc_scoring: Dict[str, Dict[str, ProcessedMCScore]]
    responses: Dict[str, Dict[str, str]]
    student_id: int
    max_stage_index: int
    max_marker: str
    stage_index: int
    total_score: int

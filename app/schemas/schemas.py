from enum import Enum

from pydantic import BaseModel


class ActionEnum(Enum):
    ACTION_0 = 0
    ACTION_1 = 1
    ACTION_2 = 2
    ACTION_3 = 3


class ActionRequestSchema(BaseModel):
    horizontalPadCoordinate: float
    verticalPadCoordinate: float
    horizontalSpeed: float
    verticalSpeed: float
    angle: float
    angularSpeed: float
    leftLegContact: int
    rightLegContact: int


class ActionResponseSchema(BaseModel):
    action: ActionEnum

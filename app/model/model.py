import numpy as np
from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO

from app.common.config import settings
from app.schemas.schemas import ActionEnum, ActionRequestSchema


def load_model(repo_id: str, filename: str) -> PPO:
    model = PPO.load(load_from_hub(repo_id, filename), print_system_info=settings.DEBUG)
    return model


def perform_inference(model: PPO, data: ActionRequestSchema) -> ActionEnum:
    data = data.model_dump()
    input_values = np.array(list(data.values()))
    action, _state = model.predict(input_values)
    return action

from huggingface_sb3 import load_from_hub
from stable_baselines3 import PPO

from app.common.config import settings

# from stable_baselines3.common.env_util import make_vec_env


def load_model(repo_id: str, filename: str) -> PPO:
    model = PPO.load(load_from_hub(repo_id, filename), print_system_info=settings.DEBUG)
    return model

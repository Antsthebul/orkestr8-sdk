import importlib
import os
from dataclasses import dataclass
from multiprocessing import Process
from pathlib import Path

from .base import Command


def _get_pid_save_location() -> Path:
    base_runs_dir = Path("~/runs")
    os.makedirs(str(base_runs_dir), exist_ok=True)
    return base_runs_dir


@dataclass
class TrainArgs:
    model_module: str


class TrainCommand(Command[TrainArgs]):
    @staticmethod
    def parse(args) -> TrainArgs:
        return TrainArgs(args.model_module)

    def _run(self):
        m = importlib.import_module(self.args.model_module)
        child_id = os.getpid()
        with open(str(_get_pid_save_location() / "run_id.txt"), "w") as f:
            f.write(f"PID: {child_id}")
        m.train()

    def run(self):
        """Imports model training module and invokes 'train' function"""
        p = Process(target=self._run)
        p.start()

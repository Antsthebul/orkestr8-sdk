import importlib
import os
from dataclasses import dataclass
from multiprocessing import Process
from pathlib import Path

from .base import Command


def _get_pid_save_location() -> Path:
    return Path("~/runs")


@dataclass
class TrainArgs:
    model_module: str


class TrainCommand(Command[TrainArgs]):
    @staticmethod
    def parse(args) -> TrainArgs:
        return TrainArgs(args.model_module)

    @staticmethod
    def _run(func):
        child_id = os.getpid()
        with open(str(_get_pid_save_location() / "run_id.txt"), "w") as f:
            f.write(f"PID: {child_id}")
        func()

    def run(self):
        """Imports model training module and invokes 'train' function"""
        m = importlib.import_module(self.args.model_module)
        p = Process(target=self._run, args=(m.train,))
        p.start()

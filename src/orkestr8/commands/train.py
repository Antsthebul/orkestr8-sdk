import importlib
from dataclasses import dataclass

from .base import Command


@dataclass
class TrainArgs:
    model_module: str


class TrainCommand(Command[TrainArgs]):
    @staticmethod
    def parse(args) -> TrainArgs:
        return TrainArgs(args.model_module)

    def run(self):
        """Imports model training module and invokes 'train' function"""
        m = importlib.import_module(self.args.model_module)
        m.train()

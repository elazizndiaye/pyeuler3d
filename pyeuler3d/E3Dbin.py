from pathlib import Path
from pyeuler3d import optPath
from pyeuler3d.config import config
import tempfile
import subprocess

"""
Contain Paths to E3D executables and methods to call them. Will consider that the binaries
are on your path by default.
"""


class E3Dbin:
    def __init__(
        self,
        prePath: optPath = None,
        solverPath: optPath = None,
        postPath: optPath = None,
    ) -> None:

        if prePath:
            self.prePath = Path(prePath)
        else:
            self.prePath = Path("E3D_PRE")

        if solverPath:
            self.solverPath = Path(solverPath)
        else:
            self.solverPath = Path("E3D_Solver")

        if postPath:
            self.postPath = Path(postPath)
        else:
            self.postPath = Path("E3D_POST")

    def callPRE(self, config: config, logPath: optPath = None):
        if logPath:
            logPath = Path(logPath)
            with logPath.open() as file:
                subprocess.run(
                    [str(self.prePath)],
                )

    def _runSim(self, exec: str, config: config, logPath: optPath):
        if not logPath:
            logFile = tempfile.NamedTemporaryFile(delete=False)
        else:
            logPath = Path(logPath)
            logFile = logPath.open()

        configPath = ""
        with logFile as file:
            subprocess.run([exec, configPath], check=True, stdout=file)

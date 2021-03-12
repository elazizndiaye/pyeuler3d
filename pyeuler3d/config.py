import tempfile
from typing import Union, Literal
from pathlib import Path
from datetime import datetime
from pyeuler3d import optPath

# Mesh formats
MESH_FORMAT_SU2 = "su2"

# Mesh types
MESH_TYPE_UNSTRUCT = "UNSTRUCTURED"
MESH_TYPE_STRUCT = "STRUCTURED"

# Speed options
SPD_OPTION_MACH = "MACH"
SPD_OPTION_VELOCITY = "VELOCITY"

# schemes
SCHEME_ROE = "ROE"
SCHEME_AVERAGE = "AVERAGE"
SCHEME_AUSM = "AUSM"

# time scheme
SCHEME_TIME_EULER_EXPLICIT = "EXPLICIT_EULER"
SCHEME_TIME_RK5 = "RK5"

# output formats
OUTPUT_FORMAT_TECPLOT = "Tecplot"
OUTPUT_FORMAT_VTU = "VTU"


class config:
    def __init__(
        self,
        INITIAL_MESH: Union[str, Path],
        comments: str = "no comments",
        PARTITION_FILES: int = 4,
        PARTITION_PATH: optPath = None,
        PRE_LOG: optPath = None,
        SPEED_OPTION: Literal[SPD_OPTION_MACH, SPD_OPTION_VELOCITY] = SPD_OPTION_MACH,
        SPEED_VALUE: float = 0.8,
        AOA: float = 0.0,
        AIRFLOW_PRESSURE: float = 101325.0,
        AIRFLOW_TEMPERATURE: float = 288.15,
        AIRFLOW_VISCOSITY: float = 1.853e-5,
        AIRFLOW_DENSITY: float = 1.2886,
        GAMMA: float = 1.4,
        GAS_CONSTANT: float = 287.058,
        SPECIFIC_HEAT: float = 1004.7,
        SCHEME: Literal[SCHEME_ROE, SCHEME_AVERAGE] = SCHEME_ROE,
        TIME_INTEGRATION: Literal[
            SCHEME_TIME_EULER_EXPLICIT, SCHEME_TIME_RK5
        ] = SCHEME_TIME_EULER_EXPLICIT,
        CFL: float = 1,
        MIN_RESIDUAL: float = 1e-14,
        MAX_ITER: int = 5000,
        SOLVER_LOG: optPath = None,
        OUTPUT_FILE: optPath = None,
        POST_LOG: optPath = None,
    ) -> None:

        # ---------------- necessary inputs ----------------

        # Mesh options
        self.INITIAL_MESH = INITIAL_MESH

        # ---------------- optional inputs -----------------

        self.comments = comments
        self.PARTITION_FILES = PARTITION_FILES
        self.SPEED_OPTION = SPEED_OPTION
        self.SPEED_VALUE = SPEED_VALUE
        self.AOA = AOA
        self.AIRFLOW_PRESSURE = AIRFLOW_PRESSURE
        self.AIRFLOW_TEMPERATURE = AIRFLOW_TEMPERATURE
        self.AIRFLOW_VISCOSITY = AIRFLOW_VISCOSITY
        self.AIRFLOW_DENSITY = AIRFLOW_DENSITY
        self.GAMMA = GAMMA
        self.GAS_CONSTANT = GAS_CONSTANT
        self.SPECIFIC_HEAT = SPECIFIC_HEAT
        self.SCHEME = SCHEME
        self.TIME_INTEGRATION = TIME_INTEGRATION
        self.CFL = CFL
        self.MIN_RESIDUAL = MIN_RESIDUAL
        self.MAX_ITER = MAX_ITER

        # optional paths
        tempDir = Path(tempfile.mkdtemp())

        self.SOLVER_LOG = SOLVER_LOG
        self.OUTPUT_FILE = OUTPUT_FILE
        self.POST_LOG = POST_LOG
        self.PARTITION_PATH = PARTITION_PATH
        self.PRE_LOG = PRE_LOG

        if not SOLVER_LOG:
            self.SOLVER_LOG = tempDir / "logSolver.txt"
        else:
            self.SOLVER_LOG = Path(SOLVER_LOG)

        if not OUTPUT_FILE:
            self.OUTPUT_FILE = tempDir / "output.dat"
        else:
            self.OUTPUT_FILE = Path(OUTPUT_FILE)

        if not POST_LOG:
            self.POST_LOG = tempDir / "logPost.txt"
        else:
            self.POST_LOG = Path(POST_LOG)

        if not PARTITION_PATH:
            self.PARTITION_PATH = tempDir / "part_#.par"
        else:
            self.PARTITION_PATH = Path(PARTITION_PATH)

        if not PRE_LOG:
            self.PRE_LOG = tempDir / "preLog.txt"
        else:
            self.PRE_LOG = Path(PRE_LOG)

    def write2file(self, path: Union[Path,str]) -> Path:
        path = Path(path)
        now = datetime.now()
        with path.open("w") as file:
            file.write(
                _fileTemplate.format(
                    author="pyeuler3d, you're favorite config file generator!",
                    title="-",
                    date=now.strftime("%d/%m/%Y %H:%M:%S\n"),
                    comments=self.comments,
                    INITIAL_MESH=self.INITIAL_MESH,
                    PARTITION_FILES=self.PARTITION_FILES,
                    PARTITION_PATH=self.PARTITION_PATH,
                    PRE_LOG=self.PRE_LOG,
                    SPEED_OPTION=self.SPEED_OPTION,
                    SPEED_VALUE=self.SPEED_VALUE,
                    AOA=self.AOA,
                    AIRFLOW_PRESSURE=self.AIRFLOW_PRESSURE,
                    AIRFLOW_TEMPERATURE=self.AIRFLOW_TEMPERATURE,
                    AIRFLOW_VISCOSITY=self.AIRFLOW_VISCOSITY,
                    AIRFLOW_DENSITY=self.AIRFLOW_DENSITY,
                    GAMMA=self.GAMMA,
                    GAS_CONSTANT=self.GAS_CONSTANT,
                    SPECIFIC_HEAT=self.SPECIFIC_HEAT,
                    SCHEME=self.SCHEME,
                    TIME_INTEGRATION=self.TIME_INTEGRATION,
                    CFL=self.CFL,
                    MIN_RESIDUAL=self.MIN_RESIDUAL,
                    MAX_ITER=self.MAX_ITER,
                    SOLVER_LOG=self.SOLVER_LOG,
                    OUTPUT_FILE=self.OUTPUT_FILE,
                    POST_LOG=self.POST_LOG,
                )
            )
        return Path("yoouupi")


_fileTemplate = """
-------------------------------------------------------------------------------
################     EULER3D Software Input file    ##################
Author : {author}
Simulation Title : {title}
Date : {date}
Comments : {comments}
-------------------------------------------------------------------------------
START
------------------- PRE-PROCESSING CONTROL -------------------
# Path to partitioned mesh files (from executable directory)
INITIAL_MESH= {INITIAL_MESH}

# Path to partitioned mesh files (from executable directory)
# Hashtag character will be replaced with file index, from 0 to Nb of partitions
PARTITION_FILES= {PARTITION_FILES}
{PARTITION_PATH}

# Path to log file for pre-processing
PRE_LOG= {PRE_LOG}

------------------- SIMULATION CONTROL -------------------
# Type of speed. Unchosen field will be ignored.
# Options : MACH -> 0
#           Velocity -> 1
SPEED_OPTION= {SPEED_OPTION}

# Velocity in m/s or Mach
SPEED_VALUE= {SPEED_VALUE}

angle of attack in degrees
AOA= {AOA}

# Airflow pressure in Pa
AIRFLOW_PRESSURE= {AIRFLOW_PRESSURE}

# Temperature in K
AIRFLOW_TEMPERATURE= {AIRFLOW_TEMPERATURE}

# Viscosity in Ns/m^2
AIRFLOW_VISCOSITY= {AIRFLOW_VISCOSITY}

# Density in kg/m^3
AIRFLOW_DENSITY= {AIRFLOW_DENSITY}

# Gamma value
GAMMA= {GAMMA}

# Gas constant in J/kg.K
GAS_CONSTANT= {GAS_CONSTANT}

# Specific heat in J/Kg.k
SPECIFIC_HEAT= {SPECIFIC_HEAT}

------------------- SOLVER CONTROL ------------------------
# Discretization of the Convective Fluxes .
# Options : ROE -> 0
#           AUSM -> 1
SCHEME= {SCHEME}

# Time integration.
# Options : EXPLICIT_EULER -> 0
#           IMPLICIT_EULER -> 1
#           RUNGE KUTTA -> 2
TIME_INTEGRATION= {TIME_INTEGRATION}

# Courant_Friedrichs-Lewy Number (CFL)
CFL= {CFL}

# Minimum residual to stop solver (RMS of density)
MIN_RESIDUAL= {MIN_RESIDUAL}

# Number of maximum iterations to stop solver
MAX_ITER= {MAX_ITER}

# Path to log file for solver
SOLVER_LOG= {SOLVER_LOG}

-------------------- POST-PROCESSING CONTROL ----------------
# Path to file output, from executable directory
OUTPUT_FILE= {OUTPUT_FILE}

# Path to log file for post-processor
POST_LOG= {POST_LOG}

END       
"""

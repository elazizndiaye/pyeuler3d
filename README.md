# pyeuler3d

Python package interfacing with the ***awesome*** [Euler3D CFD software](https://github.com/AER8875-Projet-integrateur-IV/Euler3D)


## Use

### Create a config object


```python
import pyeuler3d.config as config
import os

# All config files option for Euler3D are available as keyword parameters to this class' constructor
cfg = config.config("Path/To/Your/Mesh.su2", SPEED_OPTION = config.SPD_OPTION_MACH, SPEED_VALUE = 0.8, AOA = 1.25)

# write the config to a file
savePath = "cfg.e3d"
cfg.write2file(savePath)
with open(savePath) as configFile:
    print(configFile.read())
os.remove(savePath) 

```

    
    -------------------------------------------------------------------------------
    ################     EULER3D Software Input file    ##################
    Author : pyeuler3d, you're favorite config file generator!
    Simulation Title : -
    Date : 15/03/2021 18:11:16
    
    Comments : no comments
    -------------------------------------------------------------------------------
    START
    ------------------- PRE-PROCESSING CONTROL -------------------
    # Path to partitioned mesh files (from executable directory)
    INITIAL_MESH= Path/To/Your/Mesh.su2
    
    # Path to partitioned mesh files (from executable directory)
    # Hashtag character will be replaced with file index, from 0 to Nb of partitions
    PARTITION_FILES= 4
    /tmp/tmptgm516gw/part_#.par
    
    # Path to log file for pre-processing
    PRE_LOG= /tmp/tmptgm516gw/preLog.txt
    
    ------------------- SIMULATION CONTROL -------------------
    # Mesh orientation, this will be used during the coefficient calculations
    # Options : 0 ->  X axis
    #           1 -> -X axis
    #           2 ->  Y axis
    #           3 -> -Y axis
    #           4 ->  Z axis
    #           5 -> -Z axis
    MESH_ORIENTATION_CL= 0
    MESH_ORIENTATION_CD= 0
    
    # Reference point, this will be used for the aerodynamic coefficient calculations
    MESH_REF_POINT_X= 0.0
    MESH_REF_POINT_Y= 0.0
    MESH_REF_POINT_Z= 0.0
    
    # Sampling period, number of iterations between sampling
    SAMPLING= 500
    
    # Type of speed. Unchosen field will be ignored.
    # Options : MACH -> 0
    #           Velocity -> 1
    SPEED_OPTION= 0
    
    # Velocity in m/s or Mach
    SPEED_VALUE= 0.8
    
    angle of attack in degrees
    AOA= 1.25
    
    # Airflow pressure in Pa
    AIRFLOW_PRESSURE= 101325.0
    
    # Temperature in K
    AIRFLOW_TEMPERATURE= 288.15
    
    # Viscosity in Ns/m^2
    AIRFLOW_VISCOSITY= 1.853e-05
    
    # Density in kg/m^3
    AIRFLOW_DENSITY= 1.2886
    
    # Gamma value
    GAMMA= 1.4
    
    # Gas constant in J/kg.K
    GAS_CONSTANT= 287.058
    
    # Specific heat in J/Kg.k
    SPECIFIC_HEAT= 1004.7
    
    ------------------- SOLVER CONTROL ------------------------
    # Discretization of the Convective Fluxes .
    # Options : ROE -> 0
    #           AUSM -> 1
    SCHEME= 0
    
    # Time integration.
    # Options : EXPLICIT_EULER -> 0
    #           IMPLICIT_EULER -> 1
    #           RUNGE KUTTA -> 2
    TIME_INTEGRATION= 0
    
    # Courant_Friedrichs-Lewy Number (CFL)
    CFL= 1
    
    # Minimum residual to stop solver (RMS of density)
    MIN_RESIDUAL= 1e-14
    
    # Number of maximum iterations to stop solver
    MAX_ITER= 5000
    
    # Path to log file for solver
    SOLVER_LOG= /tmp/tmptgm516gw/logSolver.txt
    
    -------------------- POST-PROCESSING CONTROL ----------------
    # Path to file output, from executable directory
    # residuals.txt and overview.txt will also be outputted in this directory
    OUTPUT_FILE= /tmp/tmptgm516gw/output.dat
    
    # Path to log file for post-processor
    POST_LOG= /tmp/tmptgm516gw/logPost.txt
    
    END       
    


## Contribute

1. Install pipenv   (first time only)

```
    $   sudo apt install pipenv
```

2. Create your virtual environment

```
    $   pipenv  install
```

3. Launch a shell using your new virtual environment with

```
    $   pipenv  shell
```


```python

```

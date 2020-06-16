import cx_Freeze
from cx_Freeze import *

setup(
    name = "Forcefighter",
    options = {"build_exe":{"packages":['pygame']}},
    executables=[
        Executable(
            "main.py",
        )
    ]
)
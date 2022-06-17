from cx_Freeze import Executable, setup

executables = [Executable('main.py')]

setup(
    name="Jogo da Velha V_0.5",
    options={'build_exe': {'packages': ['pygame'], 'include_files': ['Imagens', 'Sons']}},
    executables=executables
)

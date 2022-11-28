@REM on crée la DLL
@REM le code doit être lancé dans une invite de
@REM commande configurée par exemple celle avec 
@REM les "outils natifs x64 VS 2017" faire bien attention
@REM à la version x64 / x86 qui doit  correspondre 
@REM à celle de python
cl /LD cmult.c

@REM on appelle CFFI qui va construire un module
python build_cffi.py
@REM 

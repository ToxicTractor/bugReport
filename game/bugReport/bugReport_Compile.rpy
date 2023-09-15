## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## this file contains all the code needed for compiling the various files.
init -1 python:
    import os, sys, platform

    ## get the directory of the python folder for the current Ren'Py installation. This is not in your project folder but in the 
    ## installation directory for Ren'Py itself. The path might be different on other machines but it should look something like:
    ## "renpy install path"/lib/"python version"
    ## it compiles to this folder as this was the only way I could get RenPy to import the compiled '.pyc' files on android devices.
    RENPY_PYTHON_DIR = os.path.join(sys.base_prefix, sys.platlibdir, f"python{sys.version_info.major}.{sys.version_info.minor}")

    ## path to the 'bugReport' folder
    BUGREPORT_PACKAGE_DIR = os.path.join(config.gamedir, "bugReport")
    SMTPLIB_PY = os.path.join(BUGREPORT_PACKAGE_DIR, "smtplib.py")
    BUGREPORTSMTP_PY = os.path.join(BUGREPORT_PACKAGE_DIR, "bugreport_smtp.py")

    ## compiles a file to a specified directory
    def CompileFile(filePath, outputDir, noPycache=True):
        import py_compile

        fileName = os.path.splitext(os.path.basename(filePath))[0]

        if not os.path.exists(filePath):
            print(f"COMPILE FILE FAILED. The file '{filePath}' does not exist!")

        sys.dont_write_bytecode = noPycache

        py_compile.compile(filePath, os.path.join(outputDir, f"{fileName}.pyc"))

        print(f"COMPILE FILE SUCCEEDED! The file '{filePath}' has been compiled to '{os.path.join(outputDir, fileName)}.pyc'.")

    def CompileFiles():
        ## if the 'bugreport_smtp.py' file exists (i.e. we are not in a build) we compile it
        if os.path.exists(BUGREPORTSMTP_PY):
            CompileFile(BUGREPORTSMTP_PY, RENPY_PYTHON_DIR)

        ## if the smtplib file has already been compiled, just return as we dont need to do it again
        if os.path.exists(os.path.join(RENPY_PYTHON_DIR, "smtplib.pyc")):
            return
        
        ## if the 'smtplib.py' file exists (i.e. we are not in a build) we compile it
        if os.path.exists(SMTPLIB_PY):
            CompileFile(SMTPLIB_PY, RENPY_PYTHON_DIR)
    
    ## call the function to compile the files
    CompileFiles()
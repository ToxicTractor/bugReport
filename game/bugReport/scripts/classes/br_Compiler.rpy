## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## this file contains all the code needed for compiling the various files.
init -1 python:
    class br_Compiler():        
        def __init__(self, compileAutomatically=True):
            
            ## get the directory of the python folder for the current Ren'Py installation. This is not in your project folder but in the 
            ## installation directory for Ren'Py itself. The path might be different on other machines but it should look something like:
            ## "renpy install path"/lib/"python version"
            ## it compiles to this folder as this was the only way I could get RenPy to import the compiled '.pyc' files on android devices.
            self.RENPY_PYTHON_DIR = os.path.join(sys.base_prefix, sys.platlibdir, f"python{sys.version_info.major}.{sys.version_info.minor}")
            
            ## path to the 'bugReport' folder
            self.BUGREPORT_PACKAGE_DIR = os.path.join(config.gamedir, "bugReport")
            
            ## path to the py files
            self.SMTPLIB_PY = os.path.join(self.BUGREPORT_PACKAGE_DIR, "scripts", "python", "smtplib.py")
            self.BUGREPORTSMTP_PY = os.path.join(self.BUGREPORT_PACKAGE_DIR, "scripts", "python", "bugreport_smtp.py")

            if (compileAutomatically):
                self.CompileFiles()


        def CompileFile(self, filePath, outputDir, noPycache=True):
            import os, sys, py_compile

            fileName = os.path.splitext(os.path.basename(filePath))[0]
            print(outputDir)

            if not os.path.exists(filePath):
                print(f"COMPILE FILE FAILED. The file '{filePath}' does not exist!")

            sys.dont_write_bytecode = noPycache

            py_compile.compile(filePath, os.path.join(outputDir, f"{fileName}.pyc"))

            print(f"COMPILE FILE SUCCEEDED! The file '{filePath}' has been compiled to '{os.path.join(outputDir, fileName)}.pyc'.")
        

        def CompileFiles(self):
            import os

            ## if the 'bugreport_smtp.py' file exists (i.e. we are not in a build) we compile it
            if os.path.exists(self.BUGREPORTSMTP_PY):
                self.CompileFile(self.BUGREPORTSMTP_PY, self.RENPY_PYTHON_DIR)

            ## if the smtplib file has already been compiled, just return as we dont need to do it again
            if os.path.exists(os.path.join(self.RENPY_PYTHON_DIR, "smtplib.pyc")):
                return
            
            ## if the 'smtplib.py' file exists (i.e. we are not in a build) we compile it
            if os.path.exists(self.SMTPLIB_PY):
                self.CompileFile(self.SMTPLIB_PY, self.RENPY_PYTHON_DIR)

    ## create a compiler and let it compile the files automatically
    br_Compiler()        

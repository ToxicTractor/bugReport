## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

## this file contains all the code needed for compiling the various files.
init -1 python:
    class br_Compiler(): 

        def __init__(self, compileAutomatically=True):
            
            if (compileAutomatically):
                self.CompileFiles()


        def CompileFile(self, filePath, outputDir, noPycache=True):
            import os, sys, py_compile

            fileName = os.path.splitext(os.path.basename(filePath))[0]

            if not os.path.exists(filePath):
                print(f"COMPILE FILE FAILED. The file '{filePath}' does not exist!")

            sys.dont_write_bytecode = noPycache

            py_compile.compile(filePath, os.path.join(outputDir, f"{fileName}.pyc"))

            print(f"COMPILE FILE SUCCEEDED! The file '{filePath}' has been compiled to '{os.path.join(outputDir, fileName)}.pyc'.")
        

        def CompileFiles(self):
            import os

            ## if the 'bugreport_smtp.py' file exists (i.e. we are not in a build) we compile it
            if os.path.exists(br_BUGREPORTSMTP_PY):
                self.CompileFile(br_BUGREPORTSMTP_PY, br_RENPY_PYTHON_DIR)

            ## if the smtplib file has already been compiled, just return as we dont need to do it again
            if os.path.exists(os.path.join(br_RENPY_PYTHON_DIR, "smtplib.pyc")):
                return
            
            ## if the 'smtplib.py' file exists (i.e. we are not in a build) we compile it
            if os.path.exists(br_SMTPLIB_PY):
                self.CompileFile(br_SMTPLIB_PY, br_RENPY_PYTHON_DIR)


    ## create a compiler and let it compile the files automatically
    br_Compiler()        

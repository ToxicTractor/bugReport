# bugReport - A Ren'Py bug reporting tool

This plug-in adds a bug report screen and the ability to send bug report emails from directly within the game. The emails the plug-in sends contain the following by default:
- The name and version of the game.
- The platform from which the bug report was sent.
- A screenshot.
- A bug category (the subject of the email).
- The file and the line which the program is currently on.
- A description of the problem by the user.

The plug-in uses the smtplib python moduel which has been included in the .zip archive. The plug-in was developed and tested only with googles SMTP service.

### Warning
Before proceeding it must be pointed out that using SMTP comes with some inherent security risks. For the plug-in to work you must put in a password for the email that you want to send the email from. As Ren'Py script files are quite easy to decompile I have implemented the sensitive parts in a python file(.py) that can then be compiled. It is not a perfect solution but it should make it harder to access any sensitive info. I still strongly recommend creating a new email account for use as the sender. 

The plug-in will attempt to place compiled python files(.pyc) in your Ren'Py install directory. This is necessary for importing the '.pyc' files on android.

### Installation
<i> This is a short installation guide. For a more indepth guide, see the .pdf in the released .zip archive. </i>

Before we begin we need to acquire an app-password this tool can use to login to the sender email.

1. Unpack the 'game' folder from the .zip archive into the Ren'Py project.
2. Open up the 'bugreport_smtp.py' python file and fill out the fields called SENDER, PASSWORD and RECEIVER with your emails and app-password.
3. Next you want to compile this python file to a .pyc file. This should be automatically done when you run your game.
4. To display a bug report button, you can show the screen called "bugReport_buttonScreen". If you just want to open up the bug report overlay you can call the python function called "OpenBugReportScreen"
5. You are done! You should now be able to send bug reports from within your game!


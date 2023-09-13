# bugReport - A Ren'Py bug reporting tool

This plug-in adds a bug report screen and the ability to send bug report emails from directly within the game. The emails the plug-in sends contain the following by default:
- The name and version of the game.
- The platform from which the bug report was sent. (Windows/Android/macOS).
- A screenshot.
- A bug category (the subject of the email).
- The file and the line on which the program is currently on.
- A description of the problem by the user.

The plug-in uses the smtplib python moduel which has been included in the .zip archive. The plug-in was developed and tested only with googles SMTP service.

### Warning
Before proceeding it must be pointed out that using SMTP the way this plug-in does comes with some inherent security risks. For the plug-in to work you must put in a password for the email that you want to send the email from. As Ren'Py script files are quite easy to decompile I have implemented this part in a pure python file that can then be compiled. It is not a perfect solution but it should make it harder to access any sensitive info. I still strongly recommend creating a new email account for use as the sender. 

### Releasing a game with the plugin
When you release your game you should remove the file called 'bugReportSMTP.py' from the 'game' folder. This is to make it harder for others to gain access to your emails and password. The game will use the compiled version of the script so bug reporting in the game is still possible.

### Installation
<i> This is a short installation guide. For a more indepth guide, see the .pdf in the released .zip archive. </i>

Before we begin we need to acquire an app-password this tool can use to login to the sender email.

1. Unpack the 'game' folder from the .zip archive into the Ren'Py project.
2. Open up the 'bugReportSMTP.py' python file and fill out the fields called SENDER, PASSWORD and RECEIVER with your emails and app-password.
3. Next you want to compile this python file to a .pyc file. In the file 'bugreport.rpy' line 193-194 will do this for you when you run your game.
4. If you compile your file using these lines it will place a .pyc file next to the uncompiled file. You should comment out the lines when you have a compiled line.
5. If you compile your file using the line in the plugin a folder called '\_\_pycache\_\_' will be created. You can delete this.
6. You are done! You should now be able to send bug reports from within your game!

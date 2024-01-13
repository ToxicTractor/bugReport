# bugReport - A Ren'Py bug reporting tool

![alt text](https://github.com/ToxicTractor/bugReport/blob/main/githubImages/main.png)

This tool allows you to send bug reports from within a Ren'Py game. The tool was designed to be as easy as possible for the players to use and thus requires no setup or login from them.

The tool is primarily supported on Windows and Android but may still work on macOS and iOS. Web builds are <b>not</b> supported!

The plug-in uses the smtplib Python module, which has been included in the '.zip' archive. The plug-in was developed and tested only with Google's SMTP service.

<p align=center>
  <img src="https://github.com/ToxicTractor/bugReport/blob/main/githubImages/email.png"/><br>
  <i>An example of an email sent by the tool.</i>
</p>

### Screenshot painter
The tool comes with a built-in screenshot painter that can be used to highlight areas of interest on the screenshots. If a user sends a report with an edited screenshot, you will receive both an unedited and an edited version of the screenshot.

![alt text](https://github.com/ToxicTractor/bugReport/blob/main/githubImages/painter.png)

### Warning
Before proceeding, it must be pointed out that using SMTP comes with some inherent security risks. For the plug-in to work, you must put in a password for the email that you want to send from. As Ren'Py script files are quite easy to decompile, I have implemented the sensitive parts in a python file (.py) that can then be compiled. It is not a perfect solution, but it should make it harder to access any sensitive information. I still strongly recommend creating a new email account for use as the sender.

The plug-in will attempt to place compiled Python files (.pyc) in your Ren'Py install directory. This is necessary for importing the '.pyc' files on Android.

### Installation
<i> This is a short installation guide. For a more in-depth guide, see the pdf in the released '.zip' archive. </i>

Before we begin, we need to acquire an app password, which this tool can use to login to the sender email.

1. Unpack the 'game' folder from the '.zip' archive into the Ren'Py project.
2. Open 'bugreport_smtp.py' located in the 'bugReport/python' folder and fill out the fields called SENDER, PASSWORD, and RECEIVER with your emails and app password.
3. Next, you want to compile this Python file into a '.pyc' file. This should be automatically done when you run your game.
4. To enable the tool in your game, you should call 'br_main.Enable()' at the start of the game. I suggest you do it at the beginning of the 'start' label.
5. You are done! You should now be able to send bug reports from within your game!

Doxywizard is a GUI front-end for configuring and running doxygen.

When you start doxywizard it will display the main window (the actual look depends on the OS used).

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_main.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_main.png)  The windows shows the steps to take to configure and run doxygen. The first step is to choose one of the ways to configure doxygen.
Wizard
> Click this button to quickly configure the most important settings and leave the rest of the options to their defaults.
Expert
> Click this button to to gain access to the [full range of configuration options](Doxygen_config.md) .
Load
> Click this button to load an existing configuration file from disk.
Note that you can select multiple buttons in a row, for instance to first configure doxygen using the Wizard and then fine tune the settings via the Expert.

After doxygen is configured you need to save the configuration as a file to disk. This second step allows doxygen to use the configuration and has the additional advantage that the configuration can be reused to run doxygen with the same settings at a later point in time.

Since some configuration options may use relative paths, the next step is to select a directory from which to run doxygen. This is typically the root of the source tree and will most of the time already be filled in correctly.

Once the configuration file is saved and the working directory is set, you can run doxygen based on the selected settings. Do this by pressing the "Start" button. Once doxygen runs you can cancel it by clicking the same button again. The output produced by doxygen is captured and shown in a log window. Once doxygen finishes, the log can be saved as a text file.

# The Wizard Dialog #


If you select the Wizard button in step 1, then a dialog with a number of tabs will appear.

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page1.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page1.png)  The fields in the project tab speak for themselves. Once doxygen has finished the Destination directory is where to look for the results. Doxygen will put each output format in a separate sub-directory.

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page2.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page2.png)  The mode tab allows you to select how doxygen will look at your sources. The default is to only look for things that have been documented.

You can also select how doxygen should present the results. The latter does not affect the way doxygen parses your source code.

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page3.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page3.png)  You can select one or more of the output formats that doxygen should produce. For HTML and LaTeX there are additional options.

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page4.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_page4.png)  Doxygen can produce a number of diagrams. Using the diagrams tab you can select which ones to generate. For most diagrams the dot tool of the [GraphViz](http://www.graphviz.org) package is needed (if you use the binary packages for Mac or Windows this tool is already included).

# Expert dialog #


The Expert dialog has a number of tab fields, one for each section in the configuration file. Each tab-field contains a number of lines, one for each configuration option in that section.

The kind of input widget depends on the type of the configuration option.
  * For each boolean option (those options that are answered with YES or NO in the configuration file) there is a check-box.
  * For items taking one of a fixed set of values (like OUTPUT\_LANGUAGE ) a combo box is used.
  * For items taking an integer value from a range, a spinbox is used.
  * For free form string-type options there is a one line edit field
  * For options taking a lists of strings, a one line edit field is available, with a `+' button to add this string to the list and a `-' button to remove the selected string from the list. There is also a `**' button that, when pressed, replaces the selected item in the list with the string entered in the edit field.
  * For file and folder entries, there are special buttons that start a file selection dialog.**


![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_expert.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_expert.png)  The get additional information about the meaning of an option, click on the "Help" button at the bottom right of the dialog and then on the item. A tooltip with additional information will appear.

# Menu options #


The GUI front-end has a menu with a couple of useful items

![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_menu.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_doxywizard_menu.png)
Open...
> This is the same as the "Load" button in the main window and allows to open a configuration file from disk.
Save as..
> This is the same as the "Save" button in the main window and can be used to save the current configuration settings to disk.
Recent configurations
> Allow to quickly load a recently saved configuration.
Set as default...
> Stores the current configuration settings as the default to use next time the GUI is started. You will be asked to confirm the action.
Reset...
> Restores the factory defaults as the default settings to use. You will be asked to confirm the action.



---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|
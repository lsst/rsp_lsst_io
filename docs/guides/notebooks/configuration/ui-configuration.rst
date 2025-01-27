#####################################
Customizing user interface appearance
#####################################

**The JupyterLab interface**

 * Under "View", selecting "Simple Interface" removes tab navigation from the main work area,
   and the left, right, and status (footer) bar can be shown or not.
 * Under "Settings - Theme", options for JupyterLab Dark and Light are available, and this theme applies
   to the entire user interface and notebooks.
 * This theme will also apply to the text editor if the text editor theme is "jupyter",
   and to the terminal if the terminal theme is "inherit".

**Jupyter Notebooks**

 * Under "View", selecting "Presentation Mode" makes the fonts larger in a Jupyter Notebook open in the main work area.
 * Under "View", selecting "Show Line Numbers" adds line numbers to the left side of every code cell or unexecuted markdown cell.
 * Under "Settings - Theme", selecting "Theme Scrollbars" makes the right-hand notebook scrollbar permanent in Dark Mode.
 * Under "Settings - Theme" it is possible to increase and decrease code font size (applies to code cells and unexecuted markdown cells) and content font size (applies to executed markdown cells).
 * It is also possible to independently increase and decrease the user interface font size, which applies to the menu bar, side bar, and status bar (footer bar).
 * All of these font size changes will be applied independent of changes to the browser font size, and apply only to Notebooks.

**Text editor**

 * Under "Settings" there are options to increase or decrease text editor font size, choose the preferred text editor indentation (spaces or tabs), and set the editor theme (includes options for, e.g., dark and light modes).
 * Text files saved with, e.g., a .py extension, will have syntax highlighting enabled automatically. If the text editor theme is "jupyter", the theme will be inherited from the JupyterLab theme.

**Terminal**

 * Under "Settings" there are options to increase or decrease the terminal font size and
   choose light or dark mode.
 * If the terminal theme is "inherit", the theme will be inherited from the JupyterLab theme.
 * Note that the text editor emacs is available, but in the terminal, and so the terminal
   options apply when using emacs in-terminal.

**Advanced Settings Editor**

 * At the bottom of the "Settings" drop-down menu is an advanced settings editor.
 * Font families, cursor blink rates, and a wide variety of other customizable parameters
   are available.

**Restore to Defaults**

 * Changes to settings are saved between Notebook Aspect sessions.
 * In the advanced settings editor, a list of the settings that have been modified floats to the top.
 * Click on any modified setting and find, at right, the option to click "Restore to Defaults" to undo every change that has been made.

# process_monitor.py

	- ❗ Disclaimer: ❗

	- This code may bear resemblance to other existing implementations, but it was written by me and intended for educational purposes only. 
	- I make no claim to be the original author of the concepts or methods implemented in this code. 
	- If you believe that any part of this code infringes upon your intellectual property rights, please contact me immediately and I will take appropriate action. 
  
  
 
 This code creates a simple process monitor using the "psutil", "qdarkstyle", and "PyQt5" libraries.

The "psutil" library provides a cross-platform interface for fetching system information, including process information. The "qdarkstyle" library provides a dark theme for the GUI, while "PyQt5" provides the necessary widgets and layouts for building the GUI.

The "ProcessMonitor" class inherits from the "QWidget" class and defines the main window for the process monitor. The "__init__" method initializes the window properties, creates the main layout, adds a table widget for displaying process information, adds buttons for refreshing the process information and ending processes, sets the layout, and displays the window.

The "display_processes" method fetches process information using "psutil" and populates the table widget with the process information. The "end_process" method terminates the selected process and removes it from the table widget.

The "if __name__ == '__main__'" block creates the "QApplication" object, creates an instance of the "ProcessMonitor" class, and executes the application.

Authors of the libraries used:

    - "psutil" - Giampaolo Rodola.
    - "qdarkstyle" - Colin Duquesnoy.
    - "PyQt5" - The Qt Company and PyQt5 developers.

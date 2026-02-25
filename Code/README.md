# Group-39-Event-Planner
ECM1414 data structures and algorithms group 39 event planner project

## How to run the event planner program
* Update your version of python to the newest one (we used 3.13.7)
* Open a terminal in the folder, making sure you're in the correct directory
* Run 'python event_planner.py' in your terminal
* Upon success you should see 'Enter filename: ' to which you can enter any valid file
* I suggest right clicking the file, then copy and pasting the relative path as your input
* Press enter ('File parsed successfully.' upon success) and wait for the program to calculate, bearing in mind it'll take much longer for larger activity quantities

## How to run the analysis and visualisation program
* Make sure to have the newest versions of python, numpy, matplotlib
* Open a terminal in the folder, making sure you're in the correct directory
* Run 'python analysis_and_visualisation.py' in your terminal
* Enter the a path of a file that has >= 28 different activities and is correctly formatted (e.g. "Input_Files/input_100.txt")
* Look at your terminal as the time it takes for the different input sizes to calculate both algorithms is shown in the console.
* Bear in mind n = 26, 28 take a few minutes to calculate for brute force
* Once all input sizes have been calculated seperate windows showing three graphs will appear, do with them as you please.

## How to run the greedy heuristic program
* Update your version of python to the newest one (we used 3.13.7)
* Open a terminal in the folder, making sure you're in the correct directory
* Run 'python greedy_heuristic.py' in your terminal
* Upon success you should see 'Enter filename: ' to which you can enter any valid file
* I suggest right clicking the file, then copy and pasting the relative path as your input
* Press enter ('File parsed successfully.' upon success)


## Brief overview of file structure

* Group-39-Event-Planner/
    * Code/
        * event_planner.py
        * README.md
        * helper.py
        * greedy_heuristic.py
        * analysis_and_visualisation.py
    * Input_Files/
        * input_10.txt
        * input_100.txt
        * input_200.txt
        * input_500.txt
        * input_1000.txt
        * input_large.txt
        * input_medium.txt
        * input_small.txt

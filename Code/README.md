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

Group-39-Event-Planner
|
|___ Code/
|    |___ event_planner.py
|    |___ README.md
|    |___ helper.py
|    |___ greedy_heuristic.py
|    |___ analysis_and_visualisation.py
|
|___ Input_Files/
    |___ input_10.txt
     |___ input_100.txt
     |___ input_200.txt
     |___ input_500.txt
     |___ input_1000.txt
     |___ input_large.txt
     |___ input_medium.txt
     |___ input_small.txt






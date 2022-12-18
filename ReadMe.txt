#@Author: Saurabh Nanda
#@Project: HW-3 Privacy in Digital Age, CSC 533, Fall 22

#File Names and Descriptions:
1.) main.py : Default Driver File, calls the source code in blocking_third_parties.py
2.)blocking_third_parties.py: Main Source code, computes unique third party domains based on cnn and macy's har files,computes domains that occur in both and performs filtering based on disconnect.json. Finally, it performs adblock based filtering based on raw_rules.txt file, which is also included in the zip folder.
3.)parse_har_fld: Modified har parser, returns list of fld's for a url
4.)parse_har_url: Modified har parser, returns list of url's and corresponding mimetypes

#Requirements
1) Install python 3 using https://www.python.org/downloads/
2) Add to environment path:
    a)Windows:https://docs.python.org/3/using/windows.html
    b)Mac: https://docs.python.org/3/using/mac.html
2) Install tld package:
command: pip install tld


#Steps to run the project:
#1) Unzip the folder
#2)Open the project (maintaining the original file structure)
#3) In any terminal based environment, like cmd or mingw, cd to the project directory containing main.py
#4) run the command:
        python main.py
#5) There are print statements within the output to let the user know what assignment question is running
#6) For any problems encountered while running the project, contact :snanda2@ncsu.edu

#Original Environment: Project made using PyCharm IDE
#Orignial run using :Python 3.9.6
#For any trouble in running the project, please contact
#author at:snanda2@ncsu.edu

# A237TG_Assignment
A237TG - Introduction to programming in Python (Grundläggande programmering i Python), Final submission



Assignment in the course Basic Programming in Python, fall semester 2023, Borås University

Purpose and Goals
The purpose of this assignment is to demonstrate, especially to yourself, that you can create a Python program based on a defined problem description where several of the skills you have acquired in the course are used. The goal of the assignment is for you, after completing the task, to have gained a further increased understanding of the basics of programming and to have gained insight into how to break down a programming task into smaller parts.

Prerequisites
The assignment consists of five subtasks that are carried out and submitted at the compulsory submission labs. The subtasks may then need to be supplemented after peer review and teacher assessment that occurs in connection with the submission. The teacher's assessment the first four times results in the assessment Usable (A) or To Be Supplemented (K). Dates, times, and instructions for peer review and supplementation are available on the assignment page for each submission occasion.

The task is to create a number of functions that are combined into a complete program with the help of a simple menu system, giving us a cohesive program. During the work, the menu system and already created functions will need to be modified to fit later tasks.

At the fifth and final submission, the entire assignment is assessed with the rating Passed (G), To Be Supplemented (K), or Failed (U). The assessment is made for each subtask separately with "OK" or "not OK". For "OK", it is required that it is acceptably correctly performed. To pass the assignment as a whole, all subtasks must be assessed as "OK". K is given if one or more subtasks need to be supplemented. U is given if one or more subtasks are missing or if it is still not correct after supplementation.

A basic rule in solving this assignment is that you may not use ready-made functions in modules that can be imported, to possibly try to simplify some calculations. Exceptions are given for the following modules that are necessary to solve reading of CSV files and plotting of diagrams:

the CSV module (see chapter 10 in Canvas) to handle CSV files
the matplotlib.pyplot module (see chapter 11 in Canvas) for plotting
There are no requirements that "input error checks" must exist, e.g., for subtask 1 where the user could enter invalid menu choices.
Some general guidelines that should be followed:

the code should be well thought out, readable, and well commented
write why code lines exist, and not what they technically do. See in the course material for discussion and examples of this (chapter 2 in Canvas Introduction and a first program example)
variables should have meaningful names
you may not submit code that generates error messages or warnings
you may not leave larger sections with old, not current, commented-out code (makes the code harder to overview)
The program code is written in VS-code - use the response file "Svarsfil_inl_1_lp3_23_A237TG.py" available in Canvas. This .py file, with your solutions in it, will be the only thing you upload upon submission in Canvas (i.e., associated .csv files do not need to be sent in). Do not change the name of the response file upon submission.
A237TG - Basic programming in Python
Assignment Description
The entire assignment is about investigating the general price development for private consumption by analyzing the Consumer Price Index (CPI) over the years 1980-2022. We will also analyze the price development for a number of goods and services during approximately the same period in more detail. The Statistical Central Bureau (SCB) is the authority responsible for updating the CPI and on their website (https://www.scb.se), you can read more about the CPI. The CPI data to be used in this assignment is saved in the file kpi.csv. We will also analyze the price development for some selected goods and services based on the information saved in the files livsmedel.csv and tjänster.csv. The following three figures show a subset of the content in each file.

Tasks
Below are the tasks. Note that you must write your functions in such an order that they are declared before they are called. All subtasks will be written in the form of functions so that you do not need to (and should not) copy and paste previously written code into your main program. You should create functions that will be reused in later subtasks, this to reduce the amount of code and make it all more manageable.

The subtasks will be performed in their entirety at a single submission lab occasion, but we will need to modify some of them at upcoming occasions to get the correct functionality in the final program.

When you are finished with the subtask, you should spend some time going through your program and ensure that it gives correct results, and double-check that the code does not violate any rule or guideline that existed under Prerequisites.

Before submission, you should also close down your program and then restart VS-code and open the program again to ensure that you are indeed running the right version of the program.

At the first submission lab, you will create your menu and some small functions that you will then use when solving the upcoming subtasks.

When you have completed all subtasks, i.e., the entire assignment, the final menu will look as follows. This also gives you an idea of what will be done in the upcoming subtasks.

Program to read in and analyze the result in tasks 1 – 5

Reads in the CSV files.
Consumer Price Index during the years 1980 – 2022.
Price development for the different categories 1980 – 2021.
Price development in percentage form for the different categories 1980 – 2021.
Comparison between different categories during the years 1980 – 2021.
Exit the program.
Choose a menu option (1–6):
Description of the menu options:
The program asks the user for the names of the three data files. Then, the three CSV files are read, and the program creates the lists kpiData, tjansteData, and livsmedelData according to task 2a. It is assumed that the CSV files are located in the same folder/directory as the .py file you are using.
Draws a diagram for the CPI during the years 1980 – 2022 according to task 3.
Draws a diagram of the price development for the different categories in the files "Goods and Services" and "Food" during the years 1980 – 2021 according to task 4.
Prints a table of the price development in percentage form for different categories in the files "Goods and Services" and "Food" during the years 1980 – 2021 according to task 2b.
Makes a comparison between different categories in the files "Goods and Services" and "Food" for the years 1980 – 2021. Lowest, highest, and diagrams are printed according to task 5.
The program is terminated and "The program is terminated" or a similar confirmation is printed on the screen.

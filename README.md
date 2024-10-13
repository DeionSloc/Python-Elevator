Python Elevator Instructions
I installed Python version 3.13.0, and built the code using Visual Studio Code with these extensions installed:
•	Python v2024.16.1
•	Python Debugger v2024.10.0
To create the elevator, I made a list of floors, and created methods for opening and closing the doors, as well as status updates for the elevator moving up and down. Directly after that I created a function called ‘elevator_up’ to simulate the elevator moving upwards
based on user input. To get around the type error I would receive when I would compare the ‘current_floor’ variable and ‘selection’ variable, I made a new variable called ‘selected_floor’ that pulled the floor number, via an index, and split it from the list.
I then wrapped the variable in an int function and ensured that it was selecting the number based off index. I did the same result for the ‘elevator_down’ function, but created a new variable, ‘selected_floor2’. 
This was done because I made the ‘selected_floor’ variable in the first function a global variable, so I could call it in the second function to use previous user input to compare that so if the user wanted to go up another floor, or down from their current floor,
they could do so, depending on the second input. 
Due to the split method used in the ‘selected_floor’ and ‘selected_floor2’ variables, a user input of ‘0’ will result in them going to the 6th floor, whereas an input of ‘6’ returns an IndexError. Otherwise, the code works as intended.

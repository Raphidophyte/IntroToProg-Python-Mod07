Julian Herndon
December 6, 2020 (late)
Foundations of Programing: Python
Assignment 07
https://github.com/Raphidophyte/IntroToProg-Python-Mod07.git

Error Handling and Pickling

Introduction:
	This Assignment 07 is almost a week late.  This is an attempt to complete it to gain at least a conceptual understanding of the purpose and syntax of error handling and pickling.  There is a partially functional script that demonstrates that while I may understand the concepts and their usefulness and application, the mechanics of the process are not yet within my skillset.  The goal was to make a simple script to demonstrate how both error handling and pickling work in python programing.

Asignment07 questions and answers: 
1)	What are the benefits of putting built-in Python command into functions?
Answer: It simplifies the work of writing code.  The built-in command already accomplishes a specific task, so by adding it to a function and “wrapping it” in additional code, that that will simplify completing the purpose of the function.  The wraparound can also alter the default behavior od the command to behave in a different way to suit the programmer’s purpose.
2)	What are the benefits of using structured error handling?
Answer:  It represents errors as objects that can be more easily dealt with and makes it possible to define your own error class types.
3)	What are the differences between a text file and a binary file?
Answer: Binary files are files that are not text files!  They are smaller and obscured as compared to text files, which are clear and public (not obscured).  Binary files may contain text, but also characters, images, etc.  Binary file contains code as well as data.  Binary files are made of bytes.  Text files have only text characters, no code.  Binary, consisting of 1s and 0s needs an interpreter to convert it back into viewable text.
4)	How is the Exception class used? 
Answer:  The following 2 URLs were helpful.  The first one (python.org) had formal, structured information that may be more useful to e I the future.  The second one (programiz) had simple and clear definitions and concise examples.

https://www.python.org/doc/essays/stdexceptions/

https://www.programiz.com/python-programming/exception-handling

The built-in python exception class is used to prevent a program from crashing if there is a problem introduced by a user or an unresolved scenario not accounted or anticipated for by the programmer.  By using a “try” clause to envelope a function, if the function cannot continue, the “except” clause will be invoked, which can contain alternate instructions on what to do next.  This will provide a path forward for the program to continue and not crash.  Potentially an entire section of the script could be skipped/ignored so that other aspects of the program can function successfully.  The exception is raised when an error occurs during runtime.
5)	How do you "derive" a new class from the Exception class?
Answer:  I believe that this is accomplished by identifying errors that could be potentially caused by a user by iterative trials.  If an error is generated and identified, then the programmer can create a new exception class that will deal with that specific error type in the future and return a message to the user.  The derived class will capture the error and allow the script to move on.
6)	When might you create a class derived from the Exception class?
Answer: When the exception class is not specific enough to address a particular user entry?
7)	What is the Markdown language? 
Answer:  It is a language used by GitHub to format plain text to create a GitHub webpage.
8)	How do you use Markdown on a GitHub webpage?
Answer: The text created in markdown is converted by Jekyll to HTML to make a static webpage.

Pickling and error handling URLs:

https://www.datacamp.com/community/tutorials/pickle-python-tutorial

https://www.datacamp.com/community/tutorials/exception-handling-python


Making the script:	
	This script tries to combine parts of lab7-1 and Assignment02.  Unfortunately, while the basic components of Assignment 02 were easily modified to fit into an error handling “try-except” format, I was unable to get the resultant data, in this case a simple quotient, to save to a binary file.   A file was created, but no data was saved to it, text or binary!  Several iterative attempts at altering portions of the code were unsuccessful.  While some of the errors were removed using by using the PyCharm debug tools, the script remains non-functional due to “pickle” remaining an “unresolved reference”.  While I feel that this should be easily solvable, I was unable to do it.
Below are a couple of screen shots, the first of which (Figure 1) shows the script running in PyCharm and demonstrating the error exception functioning.  The second one (Figure 2) shows the script running in the CMD prompt and giving an error associated with the non-functional pickling portion of the script.
 
 
 
 
Figure 1: “Herndon Assignment07.py” running in PyCharm.

 
Figure 2: Herndon Assignment07.py” at the CMD prompt.


Summary:
	Error handling is a powerful and useful tool, it is simple to implement and works well when the parameters are well defined.  The built-in Try-Except functions in Python are straightforward to implement.  Pickling is a feature of programming that seems a bit more nebulous in its purpose and application and, for now at least, remains beyond my rudimentary acquired programing skills.





References and Resources:
Python.org, (2020).  https://docs.python.org/3/library/functions.html

Intro to Programming (Python) Assignment 07.  Undated.
https://canvas.uw.edu/courses/1417585/files/67261883?module_item_id=11076737

Root, R.  Mod7 Python Programing Notes (undated)
https://canvas.uw.edu/courses/1417585/files/67261872?module_item_id=11076734

Root, R.  Mod07 Course Video.  
https://www.youtube.com/watch?v=4IkIdXJBC6o&feature=youtu.be

Starting Assignment 07 Video
https://canvas.uw.edu/courses/1417585/pages/starting-assignment-07-video?module_item_id=11076738

https://www.python.org/doc/essays/stdexceptions/

https://www.programiz.com/python-programming/exception-handling

https://www.datacamp.com/community/tutorials/pickle-python-tutorial

https://www.datacamp.com/community/tutorials/exception-handling-python




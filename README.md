# SlurDetection

You can run the program by saving it in a file named profanity_detector.py, creating two input files named tweets.txt and racial_slurs.txt, and running the following command in your terminal: The program will print the tweets and their corresponding profanity degrees in the terminal.

--python profanity_detector.py

DESCRIPTION OF THE PYTHON CODE: The calculate_profanity function takes a tweet and a set of racial slurs as input and returns the degree of profanity for the tweet as a percentage. The function first counts the number of racial slurs in the tweet using regular expressions, and then calculates the degree of profanity as the percentage of racial slurs in the tweet. The main function loads the set of racial slurs from a file, reads the tweets from another file, and calculates the degree of profanity for each tweet using the calculate_profanity function. The function then prints the tweet and its profanity degree.

Task ouput(images) and description given below:

TASK-1_Hangaman_Game:

The Hangman game is an interactive game where players guess letters to uncover a hidden word. The game begins with the choose_word() function, which randomly selects a word from a predefined list. The display_word() function creates a visual representation of the word being guessed, showing guessed letters and placeholders for unguessed letters. The main game loop is the hangman() function, which initializes variables and controls the game flow. The game continues until the word is completely guessed or the player exceeds the maximum allowed incorrect guesses. The game ends with a message indicating the player's win or loss, along with the correct word. The script concludes by calling the hangman() function to start the game.

TASK-1_Hangaman_Game_Output:
![Screenshot (68)](https://github.com/Charansaiponugoti/CodeAlpha_Python_Programming/assets/160638909/4a8073e0-38a4-4ce8-a7a4-1fe1ef9f33f7)


TASK-3_Basic_Chatbot:

This Python code creates a chatbot with a user responses dictionary, which contains responses for various user inputs. The chatbot function, called chatbot(), initiates the conversation with a greeting and prompts the user to start a conversation. It enters a loop, listens to user input, and if the input is "bye" or "exit", it chooses a random farewell message. If the input matches a key in the dictionary, it prints a response. If the input does not match any key, a default response is provided. The chatbot starts the conversation by calling chatbot(), providing pre-defined responses based on user input. It acknowledges greetings, asks about the user's well-being, responds to specific keywords, and offers farewell messages upon exiting the conversation.

TASK-3_Basic_Chatbot_Output:
![Screenshot (69)](https://github.com/Charansaiponugoti/CodeAlpha_Python_Programming/assets/160638909/f27cbd06-52ba-4307-95d9-8305c174c6ad)


TASK-4_Task_Automation_With_Python_Scripts:

This Python script organizes files from a source folder into subfolders based on their file extensions and moves them to a destination folder. It uses the shutil module for file operations and the Path class from the pathlib module for handling file paths. The function takes two arguments: source_folder (directory containing files) and destination_folder (directory where the organized files will be moved). It creates the destination folder if it doesn't already exist and gets a list of files in the source folder using Path(source_folder).glob("*"). The script iterates through each file in the source folder, checks if it's a regular file, extracts the file extension, creates a subfolder in the destination folder based on the file extension, and moves the file to the corresponding subfolder using file_path.rename(ext_folder / file_path.name). The script prints a success message after organizing the files.

TASK-4_Task_Automation_With_Python_Scripts_Output:
![Screenshot (70)](https://github.com/Charansaiponugoti/CodeAlpha_Python_Programming/assets/160638909/6a64c281-1e3f-45be-bdc3-a309d85182bc)



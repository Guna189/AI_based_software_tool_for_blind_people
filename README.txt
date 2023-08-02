# AI Based Software Tool for Blind People

## Introduction
This project is an AI-based software tool designed to assist blind people in accessing digital content and enhancing their learning experience. The software tool provides functionalities to read PDF files and access dictionary information using voice commands. The tool leverages speech recognition and text-to-speech technology to enable blind users to interact with the system seamlessly.

## Features
The software tool includes the following features:

1. **Reading PDF Files:** Blind users can instruct the tool to read a specific PDF file. The tool will use text-to-speech technology to read the content of the PDF file out loud.

2. **Searching in Dictionary:** Users can search for the meaning, synonyms, and antonyms of a word using voice commands. The tool will provide the requested information using text-to-speech output.

## Setup and Usage
1. Install the required libraries:
   - `pyttsx3`: For text-to-speech functionality.
   - `speech_recognition`: For speech recognition capabilities.
   - `PyPDF2`: For handling PDF files.
   - `PyDictionary`: For accessing word meanings, synonyms, and antonyms.

2. Set up the voice and rate of speech for the text-to-speech engine.

3. Launch the software tool and initiate communication with the user using voice prompts.

4. Ask the user to choose between reading a PDF file or searching in the dictionary.

5. If the user chooses to read a PDF file:
   - Ask the user to provide the name of the book.
   - Access the Book List to find the corresponding PDF file.
   - Read the content of the PDF file page by page using text-to-speech.

6. If the user chooses to search in the dictionary:
   - Ask the user to provide the word to be searched.
   - Use PyDictionary to fetch the meaning, synonyms, and antonyms of the word.
   - Provide the information to the user using text-to-speech output.

## Interaction Flow
1. The software tool greets the user and introduces its functionalities.

2. The tool prompts the user to choose between reading a PDF file or searching in the dictionary.

3. Based on the user's choice, the tool follows the appropriate path:
   - If the user chooses to read a PDF file, the tool asks for the name of the book.
   - If the user chooses to search in the dictionary, the tool asks for the word to be searched.

4. The user's responses are captured using speech recognition technology.

5. The tool processes the user's input and performs the requested action.

6. The tool utilizes text-to-speech technology to provide output and interact with the user.

7. The user can continue to interact with the tool until they decide to exit.

## Conclusion
The AI-based software tool for blind people offers a user-friendly interface to access digital content and dictionary information using voice commands. By integrating speech recognition and text-to-speech capabilities, the tool empowers blind individuals to explore books and obtain word meanings effortlessly. This project aims to enhance the accessibility and learning experience of visually impaired users, making digital content more inclusive and available to all.

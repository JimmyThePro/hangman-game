# **HANGMAN**
"Hangman" is a python terminal game, which runs in a terminal on Heroku (https://www.heroku.com/).
This fun little game is for people that enjoy to challenge themself, and of course for "hangman game" addicts.
Users get a random word they need to guess, one letter at the time. But beware, if you get 6 failed guesses, you lose!
Sounds easy right? Well... it's not! Go try and see: https://jimmythepro.github.io/einstein-quiz/
<br/><br/>

![hangman game](assets/images/responsive.png)

## How to play

This game is a classic hangman game, you can read more about hangman here: https://en.wikipedia.org/wiki/Hangman_(game)

    - This game will start when landing on this domain: 
    - First, user needs to enter a Name.
    - User will get a random "Secret word" from our library (100 secret words added, animalwords only).
    - And now the user can start to guess a letter. User will only see "underscores" as the secret word, so if the secret word is "LION", the user will see "_ _ _ _".
    - User can guess one letter at the time, and get '6 fails' until he/she fails the game.
    - If user manage to guess all letters right in the secret word, it's a win!
<br/><br/>

![image](assets/images/main_page.png)

## Features

* **Existing Features**

    - The secret word is randomly picked from the 'secret_words' file (animal words).
    - User have no clue what the secret word is, it shows "underscores" as letters to the user.
    - Maintain number of fails.
    - Accepts user inputs.
    - Input validation and error checking.
        - User must enter a Name when starting.
        - User must enter one letter when guessing.
        - User cannot guess the same letter twice.
        - User cannot guess with 2+ letters, ONE letter only for each guess.
        - User cannot enter 'numbers' or 'special characters' when guessing a letter.
    - Data maintained in the class instance Hangman.
    - An 'ascii hangman art' is shown for each failed letters guessed.
    - When a user win, he/she can play a new game or quit game.
    - When a user lose, he/she can play a new game or quit game.

<br/><br/>

![image](assets/images/logo_favicon.png)

* **Future Features**

    - Add more "Secret words".
    - Add categories for secret words (exampel: press '1' for animal words / press '2' for city words etc).
<br/><br/>

## Data Model

I used a Hangman class as my model. The Hangman class stores the secret word.
The class also has methods to help play the game, such as tracks letters in a secret word, track if a guessed letter is correct and also track if/when a user wins.

## UX

A Hangman enthusiast or a thrill seeker will find this game very fun!
I bet the user will play until he/she falls asleep.
<br/><br/>

* **User stories**

    - NEW USER: I am interested in Hangman games, and want to guess as many secret words I can!
    - RETURNING USER: User can show their family/friends this game, and play together.
<br/><br/>

* **Game goal**

    - The goal of the game is to have fun and test your 'hangman skills'.
<br/><br/>

* **Business owner**

    - I want to entertain my users, and provide them with many laughs!
    - This site will add alot of positive vibes to the users.
<br/><br/>

* **Wireframes**

    - I made a flow chart to get a better understanding of the game steps.
<br/><br/>

![flow chart](assets/images/wireframe.png)

## Testing

* **Validator testing**

    - PEP8
        - No errors or warnings detected when checked on: http://pep8online.com/
<br/><br/>

![lighthouse score](assets/images/lighthouse.png)

## Bugs

    - No bugs detected.

## Unfixed bugs

    - No unfixed bugs.

## Technologies

* **Languages used**

    - Python

## Programs

    - Gitpod, used for code writing.
    - Githud, store data.
    - Git, version control.

## Deployment

* **Was deployed to Github pages. The steps are:**

    - Github repository --> settings tab --> source section drop-down menu --> main
    - When selected "main", page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
    - The site link: https://jimmythepro.github.io/einstein-quiz/

## Credits

Also got help and tips from my mentor Adegbenga Adeye.
To complete this 'Einstein Quiz' I used Code Institute student template: https://tinyurl.com/2p8mh8y9
<br/><br/>

* **Content**

    - Question examples picked from https://tinyurl.com/4wparj3a / https://tinyurl.com/3c7c3nn4 / https://tinyurl.com/ecxc7tsf
    - Fonts (Bubblegum Sans, Open Sans) imported from https://fonts.google.com/
    - Learned reload button here: https://tinyurl.com/39e3f3pn
    - Learned "checked radiobutton" code here: https://tinyurl.com/59ddenvd
    - Got information to uncheck radio buttons here: https://tinyurl.com/yc5a78th
    - Color palette picked from https://colorhunt.co/
    - Used Tinyurl to shorten the links - https://tinyurl.com/app/
<br/><br/>

* **Media**

    - All the images taken from https://www.pexels.com/ and https://www.freepik.com/
    - The icons is taken from https://fontawesome.com/
    - Used GIMP/paint for scaling the images, and GIMP for favicon image - https://www.gimp.org/
<br/><br/>

* **Colors and fonts**

    - Background color: #ffffff
    - Body font color: #252A34
    - Heading font color: #676FA3
    - Button color: #f8a6aa
    - Fonts used: 'Bubblegum Sans' and 'Open Sans'.
<br/><br/>

[Back to Top](#Einstein-Quiz)
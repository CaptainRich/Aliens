# $`\textcolor{blue}{\text{Aliens}}`$
An Alien shooter game, illustrating the implementation of 'pygame'.
Richard Ay (February 2024, *updated February 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Sample Display](#sample-display)

## Setup

*To use this program, activate the 'virtual environment' "AlienEnv".  

## Environment
A virtual environment is created so that the installation of PyGame remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "AlienEnv" --upgrade-deps --prompt="AlienEnv"'**

To start/stop the virtual environment, use the commands: **'AlienEnv\scripts\activate'** or **'deactivate'**. Once activated, the virtual environment will change the (terminal) prompt from (PS) to (AlienEnv).

After starting the virtual environment, PyGame can be installed with the command:  
**'python -m pip install pygame'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show pygame'**. 


## Usage
From VSCode, by issuing the command 'python directory-scan.py' in the Terminal window. For VS Code it is important to change the Terminal from "Git Bash" to "Power Shell". Once in Power Shell, the command "python aliens.py" will run the file with the game screen displayed.  Note the suffix ".py" is required.

The Alien ship can be moved left/right using the keyboard 'arrow' keys.  The game can be stopped by pressing 'q', or the 'X" in the upper right of the window frame.


## References
1. Python Crash Course, Eric Matthes, No Starch Press, 2023. Chapters 12-14.  


## File List
**aliens.py** - the main game file, invoked to play the game.  
**bullet.py** - a class module controlling the firing of bullets.   
**button.py** - a class module to implement a 'play' button for the game.   
**game_stats.py** - a class module to track game statistics.  
**settings.py** - a class module managing the game settings.  
**ship.py** - a class module managing the defending ship setup, drawing, and movement.  
**ufos.py** - a class module managing the alien ships (ufos).

**/images** - a subdirectory with game images

## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- sys
- pygame

## Sample Display
The image below shows a sample game screen:
![Sample Display](https://github.com/CaptainRich/Aliens/blob/develop/Images/game-screen.png)

The image below depicts a (class) mind-map for the game program:
![Sample Display](https://github.com/CaptainRich/Aliens/blob/develop/Images/Program-MindMap.png)


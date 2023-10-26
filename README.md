# Ultimatum
An otree python game
# Project Description
This is a short version of the full [ultimatum game](https://en.wikipedia.org/wiki/Ultimatum_game)

Page 1 - Player 1 is told that he has been endowed with Ksh 200 and is asked to send any amount between 0 and 200 to Player 2.

Page 2 - Player 3 sees the amount that Player 1 has decided to send to Player 2 and from this, he will decide to either Punish or Not Punish Player 1.

Page 3 - Results Page, Player 1 and Player 2 will be notified of the results in this way

Player 1:
The amount he decided to send to player 2
The decision that Player 3 made
The payout that he gets.

Player 2:
The amount that Player 1 decided to send him
The decision that Player 3 made
The payout that he gets


## Getting Started

These instructions will help you set up the project environment and get it running on your local machine.

### Prerequisites

To run this project, you will need [Conda](https://docs.conda.io/en/latest/miniconda.html) installed on your system.

### Create a Conda Environment

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/pgm_githumbi/ultimatum.git
   ```

2. cd into your-project directory

Create a Conda environment and activate it.


```bash

conda env create -f environment.yml
conda activate busara_interview
```
 The environment.yml file contains a list of required packages and their versions.


 3. Run the project
    ```bash
     otree devserver
    ```

[BSI_106.webm](https://github.com/pgm-githumbi/ultimatum/assets/85244060/a4ea2849-3f0c-4896-b939-7386855dcf92)



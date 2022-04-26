"use strict";

const player1 = document.querySelector(".player1");
const player2 = document.querySelector(".player2");
const scorePlayer1 = document.querySelector(".score-player1");
const scorePlayer2 = document.querySelector(".score-player2");
const currentElement = document.querySelector(".current-score");
const btnNew = document.querySelector(".btn-new");
const btnRoll = document.querySelector(".btn-roll");
const btnHold = document.querySelector(".btn-hold");
const diceElement = document.querySelector(".dice");

let scores, currentScore, activePlayer, playing;

// Functions
const newGame = function () {
    scores = [0, 0];
    currentScore = 0;
    activePlayer = 0;
    playing = true;

    scorePlayer1.textContent = 0;
    scorePlayer2.textContent = 0;
    currentElement.textContent = 0;

    diceElement.classList.add("hidden");
    player1.classList.add("player-active");
    player1.classList.remove("winner");
    player2.classList.remove("winner");
    player2.classList.remove("player-active");
};

const switchPlayer = function () {
    player1.classList.toggle("player-active");
    player2.classList.toggle("player-active");
    activePlayer = activePlayer === 0 ? 1 : 0;
    currentElement.textContent = 0;
    currentScore = 0;
};

// Start Game
newGame();

// Start New Game
btnNew.addEventListener("click", newGame);

// Rolling dice
btnRoll.addEventListener("click", function () {
    if (playing) {
        // 1. Random number
        const diceNumber = Math.trunc(Math.random() * 6) + 1;
        // 2. Display dice
        diceElement.src = `assets/img/dice-${diceNumber}.png`;
        diceElement.classList.remove("hidden");
        // 3. Check for rolled 1
        if (diceNumber !== 1) {
            // Add dice to current score
            currentScore += diceNumber;
            currentElement.textContent = currentScore;
        } else {
            // Switch player
            switchPlayer();
        }
    }
});

// Hold score
btnHold.addEventListener("click", function () {
    if (playing) {
        // 1. Add current score to active player's score
        scores[activePlayer] += currentScore;
        document.querySelector(`.score-player${activePlayer + 1}`).textContent = scores[activePlayer]; //prettier-ignore
        // 2. Check if player's score is over 100
        if (scores[activePlayer] >= 100) {
            // Finish the Game
            document.querySelector(`.player${activePlayer + 1}`).classList.add("winner"); //prettier-ignore
            diceElement.classList.add("hidden");
            playing = false;
        } else {
            // Switch player
            switchPlayer();
        }
    }
});

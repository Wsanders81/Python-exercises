"use strict";


const $msg = $("#msg");
const $guessInput = $("#guess-input");
const $score = $("#score-value");
const $hiScore = $("#high-score-value");
const $timer = $("#timer");

let score = 0;
let highScore = 0;
let seconds = 60;
let words = [];

const showScore = () => $score.text(score);
const showTimer = () => $timer.text(seconds);
const timer = setInterval(gameTimer, 1000);

async function gameTimer() {
  seconds -= 1;
  showTimer();
  if (seconds === 0) {
    gameOver();
    await scoreGame();
    $('#timer').text('0')
    clearInterval(timer);
  }
}

function gameOver() {
  alert("Times Up!");
}

function resetClass() {
  if ($msg.hasClass("success") || $msg.hasClass("error")) {
    $msg.removeClass();
  }
}

async function scoreGame() {
  $("#guess-form").hide();

  const res = await axios.post(`/post-score`, { score: score });

  if (res.data.brokeRecord === true) {
    $msg
      .show()
      .addClass("success")
      .text(`Congratulations! Your new highscore is ${score}!`);
  } else {
  }
}

$("#guess-form").on("submit", async function (e) {
  e.preventDefault();
  resetClass();
  let word = $("#guess-input").val();
  let wordUpper = word.toUpperCase();

  const res = await axios.get(`/check-for-answer`, {
    params: { word: word },
  });

  if (words.indexOf(word) !== -1) {
    // resetClass();
    $msg
      .show()
      .addClass("error")
      .text(`Sorry, "${wordUpper}" has already been used`);
    $guessInput.val("");
    return;
  } else if (res.data.result === "not-word") {
    $msg.show().addClass("error").text(`Sorry, "${wordUpper}" is not a word`);
  } else if (res.data.result === "not-on-board") {
    $msg
      .show()
      .addClass("error")
      .text(`Sorry, "${wordUpper}" is not on the board`);
  } else if (res.data.result === "ok") {
    let points = word.length;
    $msg
      .show()
      .addClass("success")
      .text(`Great job! "${wordUpper}" = ${points} points `);
    score += points;
    words.push(word);
    showScore();
  }
  $guessInput.val("");
});

showTimer();

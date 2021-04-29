"use strict";

class Boggle {
  constructor(boardName, secs = 60) {
    // this.$msg = $("#msg");
    // this.$guessInput = $("#guess-input");
    // this.$score = $("#score-value");
    // this.$hiScore = $("#high-score-value");
    // this.$timer = $("#timer");

    // this.highScore = 0;
    this.seconds = secs;
    this.showTimer();
    this.score = 0;
    this.words = [];
    this.board = ("#", +boardName);

    this.timer = setInterval(this.gameTimer.bind(this), 1000);
    $("#guess-form", this.board).on("submit", this.submitHandler.bind(this));
  }

  showTimer() {
    $("#timer", this.board).text(this.seconds);
  }

  showScore() {
    $("#score-value", this.board).text(this.score);
  }

  async gameTimer() {
    this.seconds -= 1;
    this.showTimer();
    const $timer = $('#timer')
    if(this.seconds === 10) {
      $timer.addClass('error-color')
    }
    if (this.seconds === 0) {
      
      $("#timer", this.board).text("0");
      clearInterval(this.timer);
      await this.scoreGame();
    }
  }

  gameOver() {
    setTimeout(alert("Times Up!"), 2000);
  }

  resetClass() {
    if (
      $("#msg", this.board).hasClass("success") ||
      $("#msg", this.board).hasClass("error")
    ) {
      $("#msg", this.board).removeClass();
    }
  }
  addWord(word){
    const $li = $(`<li>${word}</li>`); 
    const $ul = $('#word-ul'); 
    $ul.append($li);
  }

  async scoreGame() {
    $("#guess-form", this.board).hide();

    const res = await axios.post(`/post-score`, { score: this.score });

    if (res.data.brokeRecord === true) {
      const $score = $("#msg-score"); 
      $("#game-over-modal").show();
      $('#high-score-msg').show();

      $score.text(this.score);
    } else { 
      const $score = $("#msg-score"); 
      $("#game-over-modal").show();

      $score.text(this.score);
      
    }
  }
  async submitHandler(e) {
    // $("#guess-form").on("submit", async function (e) {
    e.preventDefault();
    this.resetClass();
    const $word = $("#guess-input", this.board);
    let word = $word.val();
    let wordUpper = word.toUpperCase();

    const res = await axios.get(`/check-for-answer`, {
      params: { word: word },
    });
    console.log(res)

    if (this.words.indexOf(word) !== -1) {
      // resetClass();
      $("#msg", this.board)
        .show()
        .addClass("error")
        .text(`Sorry, "${wordUpper}" has already been used`);
      $("guess-input").val("");
      return;
    } else if (res.data.result === "not-word") {
      $("#msg", this.board)
        .show()
        .addClass("error")
        .text(`Sorry, "${wordUpper}" is not a word`);
    } else if (res.data.result === "not-on-board") {
      $("#msg", this.board)
        .show()
        .addClass("error")
        .text(`Sorry, "${wordUpper}" is not on the board`);
    } else if (res.data.result === "ok") {
      let points = word.length;
      $("#msg", this.board)
        .show()
        .addClass("success")
        .text(`Great job! "${wordUpper}" = ${points} points `);
      this.addWord(word);
      this.score += points;
      this.words.push(word);
      this.showScore();
    }
    $("#guess-input").val("");
  }
  // }
}

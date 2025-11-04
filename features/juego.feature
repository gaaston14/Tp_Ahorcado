Feature: Hangman Game Web
  As a player, I want to interact with the hangman web page
  so I can win or lose a match.

  Background:
    Given the user is on the home page

  @set_word_python
  Scenario: 1. Win a match by guessing the word
    When the user guesses the word "python"
    Then the user sees the victory message "¡GANASTE!"

  @set_word_python
  Scenario: 2. Lose a match by 6 incorrect letters
    When the user guesses the letter "z"
    And the user guesses the letter "q"
    And the user guesses the letter "w"
    And the user guesses the letter "j"
    And the user guesses the letter "k"
    And the user guesses the letter "x"
    Then the user sees the defeat message "¡PERDISTE!"
    And the user sees the revealed secret word "PYTHON"

  @set_word_python
  Scenario: 3. Guess a correct letter
    When the user guesses the letter "p"
    Then the user sees the progress "p _ _ _ _ _"

  @set_word_python
  Scenario: 4. Guess a repeated letter
    When the user guesses the letter "z"
    And the user guesses the letter "z"
    # ARREGLO: Buscamos solo una parte del mensaje para evitar error de comillas
    Then the user sees the message "Ya habías intentado la letra"
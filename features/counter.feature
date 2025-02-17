Feature: Counter Application
  As a user, I want to use a counter application so that I can increase, decrease, or reset the count.

  Scenario: Increment the counter
    Given the counter starts at 0
    When I press the "Increment" button
    Then the counter should display 1

  Scenario: Decrement the counter
    Given the counter starts at 1
    When I press the "Decrement" button
    Then the counter should display 0

  Scenario: Reset the counter
    Given the counter starts at 5
    When I press the "Reset" button
    Then the counter should display 0

  Scenario: Multiple increments
    Given the counter starts at 0
    When I press the "Increment" button 3 times
    Then the counter should display 3

  Scenario: Multiple decrements
    Given the counter starts at 5
    When I press the "Decrement" button 2 times
    Then the counter should display 3

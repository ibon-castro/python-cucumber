import requests
from behave import given, when, then

BASE_URL = "http://34.207.242.140:5000"  # Assuming the app is running locally

@given('the counter starts at {start:d}')
def step_given_counter_starts(context, start):
    # Initialize the counter at the given starting value
    context.start_value = start
    context.response = requests.get(BASE_URL)  # Get the initial page to start the app

    # Manually set the counter to the start value via the reset endpoint
    if start != 0:
        requests.post(f"{BASE_URL}/reset")  # Reset the counter to 0
        for _ in range(start):
            requests.post(f"{BASE_URL}/increment")  # Increment to the start value

@when('I press the "{button}" button')
def step_when_press_button(context, button):
    # Simulate button presses (Increment, Decrement, Reset)
    if button == "Increment":
        context.response = requests.post(f"{BASE_URL}/increment")
    elif button == "Decrement":
        context.response = requests.post(f"{BASE_URL}/decrement")
    elif button == "Reset":
        context.response = requests.post(f"{BASE_URL}/reset")

@when('I press the "{button}" button {times:d} times')
def step_when_press_button_multiple(context, button, times):
    # Simulate multiple button presses
    for _ in range(times):
        if button == "Increment":
            context.response = requests.post(f"{BASE_URL}/increment")
        elif button == "Decrement":
            context.response = requests.post(f"{BASE_URL}/decrement")

@then('the counter should display {expected:d}')
def step_then_counter_should_display(context, expected):
    # Check if the counter in the response page matches the expected value
    assert str(expected) in context.response.text, f"Expected {expected}, but got a different count."

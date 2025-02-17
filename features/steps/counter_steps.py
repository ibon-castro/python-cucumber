from behave import given, when, then
from app import CounterApp
import tkinter as tk

@given('the counter starts at {start:d}')
def step_given_counter_starts(context, start):
    context.root = tk.Tk()
    context.app = CounterApp(context.root)
    context.app.count = start
    context.app.update_label()

@when('I press the "{button}" button')
def step_when_press_button(context, button):
    if button == "Increment":
        context.app.increment()
    elif button == "Decrement":
        context.app.decrement()
    elif button == "Reset":
        context.app.reset()

@when('I press the "{button}" button {times:d} times')
def step_when_press_button_multiple(context, button, times):
    for _ in range(times):
        if button == "Increment":
            context.app.increment()
        elif button == "Decrement":
            context.app.decrement()

@then('the counter should display {expected:d}')
def step_then_counter_should_display(context, expected):
    assert context.app.count == expected, f"Expected {expected}, but got {context.app.count}"

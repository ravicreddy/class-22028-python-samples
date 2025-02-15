import random

"""Plays a country capitals quiz."""


def play_quiz():
    countries_and_capitals = {
        "Afghanistan": "Kabul",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "India": "New Delhi",
        "Japan": "Tokyo",
        "Mexico": "Mexico City",
        "Russia": "Moscow",
        "United States": "Washington, D.C."
    }

    countries_and_capitals['Sweden'] = "Stockholm"


    score = 0
    num_questions = 5

    for abc in range(num_questions):
        country = random.choice(list(countries_and_capitals.keys()))
        capital = countries_and_capitals[country]

        answer = input(f"What is the capital of {country}? ")

        if answer.lower() == capital.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The capital is {capital}.")

    print(f"\nYou got {score} out of {num_questions} questions correct.")


play_quiz()

#!/usr/bin/env python

import click
import json

def luhn_test(purported):
    LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)  # sum_of_digits (index * 2)
    if not isinstance(purported, str):
        purported = str(purported)
    try:
        evens = sum(int(p) for p in purported[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(p)] for p in purported[-2::-2])
        return ((evens + odds) % 10 == 0)
    except ValueError:  # Raised if an int conversion fails
        return False


@click.group("cli")
def cli():
    pass

@cli.command("scrape-cardlist")
def create_keylist():
    cards = json.load(open("cards.json"))
    card_numbers = (card["CreditCard"]["CardNumber"] for card in cards)
    for number in card_numbers:
        print(number)

@cli.command("get-invalid")
@click.argument("NUMBERS")
def solve(numbers):
    for line in open(numbers):
        line = line.strip()
        if not luhn_test(line):
            print(line)

cli()

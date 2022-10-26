#!/usr/bin/env python3
from brain_games.games_logic import common_games_logic
from brain_games.games.prime import prime_number_or_not


def main():
    common_games_logic(function=prime_number_or_not)


if __name__ == '__main__':
    main()

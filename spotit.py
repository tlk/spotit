#!/bin/env python3

import random


def main():
    random.seed(42)
    cards = get_cards()
    symbols = get_symbols()
    svgs = render_to_svgs(cards, symbols)
    html = render_to_html(svgs)
    print(html, end="")


def get_cards(order=7):
    from sage.all import designs, GF

    # See https://stackoverflow.com/a/31154452/936466
    PG = designs.ProjectiveGeometryDesign(2, 1, GF(order), point_coordinates=0)
    cards = PG.blocks()

    random.shuffle(cards)
    [random.shuffle(card) for card in cards]
    return cards


def get_symbols(filename="config/emojis.txt"):
    import emoji

    with open(filename, "r") as f:
        lines = f.readlines()

    symbols = []
    for line in lines:
        line = line.strip()

        if line.startswith("#"):
            continue

        if line:
            symbol = emoji.emojize(line)
            symbols.append(symbol)

    random.shuffle(symbols)
    return symbols


def render_to_svgs(cards, symbols):
    template = get_template("config/template.svg")

    svgs = []
    for card_index in range(len(cards)):
        card = cards[card_index]
        replacements = {}

        title = f"Card #{card_index+1}"
        replacements["TITLE"] = title

        for symbol_index in range(len(card)):
            card_symbol = card[symbol_index]
            replacements[f"S{symbol_index+1}"] = symbols[card_symbol]

        svg = fill_template(template, replacements)
        svgs.append(svg)

    return svgs


def render_to_html(svgs):
    template = get_template("config/template.html")

    body = "\n".join(svgs)
    html = template.replace("BODY_CONTENT", body)

    return html


def get_template(filename):
    with open(filename, "r") as f:
        template = f.read()
    return template


def fill_template(template, replacements):
    content = template.replace("\n", "")
    for key, value in replacements.items():
        content = content.replace(key, value)
    return content


if __name__ == "__main__":
    main()

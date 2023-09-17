# Spot it!
See https://tlk.github.io/spotit/cards.html for a set of 57 cards inspired by the popular [Spot it!](https://www.spotitgame.com) game.


## Mathematical background
Apparently, this game is built on what is called a Finite projective plane of order 7.

See https://images.math.cnrs.fr/Dobble-et-la-geometrie-finie.html (in French), or these comments on Stackoverflow:
- https://stackoverflow.com/a/6240394/936466
- https://stackoverflow.com/a/31154452/936466


## From theory to emojis
The spotit.py script create cards from a template file with placeholders named S1, S2 .. S8.

The placeholders are replaced with emojis to make the cards colorful.

Finally, all cards are combined into a [single file cards.html](https://tlk.github.io/spotit/cards.html) that can be printed out.


## Customizing the cards
 Template file                       |  Example card
:-----------------------------------:|:--------------------------------:
 ![template](./config/template.svg)  |  ![example](./docs/example.svg)

The [template file](https://github.com/tlk/spotit/blob/main/config/template.svg) is in [SVG-format](https://en.wikipedia.org/wiki/SVG) and can be customized using free software such as [macSVG](https://macsvg.org).

It is also possible to [customize the emojis](https://github.com/tlk/spotit/blob/main/config/emojis.txt) used to generate the cards.
Be aware that emojis may not look the same on different devices and operating systems.


## Links
- https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/designs/block_design.html#sage.combinat.designs.block_design.ProjectiveGeometryDesign
- https://doc.sagemath.org/html/en/reference/finite_rings/sage/rings/finite_rings/finite_field_constructor.html
- https://carpedm20.github.io/emoji/
- https://github.com/WRadigan/pySpot-It


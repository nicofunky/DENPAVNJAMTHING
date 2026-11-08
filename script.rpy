# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nn = Character(color="#d3e8ea", kind=nvl,what_textalign=0.0)
define nc =Character(color="#ffcccc", kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show chunni1

    nvl show dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    nn "Stars."
    nn "Stars continue to rain down their light from above, regardless of how we feel.{p}They’re indifferent to our existence.{p}They’re unbothered by the continuous gaze of mankind.{p}They don’t mind all the myths and legends we build up around them.{p}They accept any visitors or passerbys, regardless of their status."
    nn "They continue to shine, regardless of it all, until they die."
    nvl clear
    nc "penis penis balls"
    nvl clear
    nn "penis balls"
    nn "more text."
    nc "more test text."
    nvl clear
    nn "penis."

    # This ends the game.

    return

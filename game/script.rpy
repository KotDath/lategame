# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define floppa = Character("Floppa")
define bananacat = Character("Banana Cat")
define spincat = Character("Spin Cat")

image floppa_idle = "images/floppa/idle.png"
image floppa_talk = "images/floppa/talk.png"


define spincat_images = "images/spincat/output_"
define total_spincat_frames = 59  # Change this to the number of frames you have

# Create a list of images for the animation
define spincat_animation = Animation(
    *[f"{spincat_images}{str(i).zfill(3)}.png" for i in range(1, total_spincat_frames + 1)],
    duration=0.1
)

image spincat_animation:
    "images/1.png"
    2.00
    "images/2.png"
    2.00
    "images/3.png"
    2.00
    "images/4.png"
    2.00
    repeat

label start:

    scene bg room

    show floppa_idle


    floppa "A."

    floppa "B"

    show spincat_animation
    pause(1.0)
    "The animation has finished."


    return

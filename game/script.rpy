# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    def next_spincat_frame(t, st, at):
        global animation_frame
        global spincat_frame
        if animation_frame < 59:
            animation_frame += 1
            spincat_frame = f"images/spincat/output_{animation_frame:03d}"
        else:
            animation_frame = 1
            spincat_frame = f"images/spincat/output_{animation_frame:03d}"


define floppa = Character("Floppa")
define bananacat = Character("Banana Cat")
define spincat = Character("Spin Cat")

image floppa_idle = "images/floppa/idle.png"
image floppa_talk = "images/floppa/talk.png"


define spincat_images = "images/spincat/output_"
define total_spincat_frames = 59  # Change this to the number of frames you have

image spincat_animation:
    "[spincat_frame].png"
    function next_spincat_frame
    pause 0.016
    repeat

label start:

    scene bg room

    show floppa_idle


    floppa "A."

    floppa "B"

    hide floppa_idle

    $animation_frame = 1
    $spincat_frame = "images/spincat/output_001"
    show spincat_animation

    pause(1.0)
    "The animation has finished."


    return

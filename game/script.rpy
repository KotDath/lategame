# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    class AnimationController():
        def __init__(self, images_dir, max_frame_count, interval):
            self.animation_frame = 1
            self.max_frame_count = max_frame_count
            self.interval = interval
            self.images_dir = images_dir
            self.current_frame = f"{images_dir}/output_001.png"
        
        def next_frame(self, a, b, c):
            if self.animation_frame < self.max_frame_count:
                self.animation_frame += 1
                self.current_frame = f"{self.images_dir}/output_{self.animation_frame:03d}.png"
            else:
                self.animation_frame = 1
                self.current_frame = f"{self.images_dir}/output_{self.animation_frame:03d}.png"

transform move_diagonal:
    xpos 0.1
    ypos 0.1
    linear 4.0 xpos 0.5 ypos 0.5
    linear 4.0 zoom 2


define floppa = Character("Floppa")
define bananacat = Character("Banana Cat")
define spincat = Character("Spin Cat")

image floppa_idle = "images/floppa/idle.png"
image floppa_talk = "images/floppa/talk.png"
image spincat_idle = "images/spincat/idle.png"


define spincat_sound_normal = "audio/spincat/normal.mp3"

default spincatController = AnimationController("images/spincat/spin", 59, 0.033)

image bg bmstu = "images/backgrounds/bmstu.jpg"

image spincat_animation:
    xalign 0.5
    yalign 0.5
    "[spincatController.current_frame]"
    function spincatController.next_frame
    pause spincatController.interval
    repeat

label start:

    scene bg bmstu
    with Dissolve(.5)

    show floppa_idle


    floppa "ВНИМАНИЕ"

    floppa "ГИФКА"

    hide floppa_idle

    show spincat_animation at move_diagonal
 
    play sound spincat_sound_normal loop

    pause(8)

    stop sound

    hide spincat_animation

    show spincat_idle:
        xalign 0.5
        yalign 0.5

    pause(3)

    play sound spincat_sound_normal loop
    
    "Сухарик."


    return

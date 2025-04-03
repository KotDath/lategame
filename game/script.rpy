# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    from animation import AnimationController

    _preferences.set_volume('music', 0.01)
    renpy.restart_interaction()


transform move_diagonal:
    xpos 0.1
    ypos 0.1
    linear 4.0 xpos 0.5 ypos 0.5
    linear 4.0 zoom 2

transform move_to_door:
    xpos 0.85
    ypos 0.85
    linear 2.0 xpos 0.3 ypos 0.85
    linear 2.0 xpos 0.35 ypos 0.6

transform move_out_university:
    xpos 0.85
    ypos 0.85
    linear 2.0 xpos 1.2 ypos 0.85


transform move_in_university:
    xpos 0.85
    ypos 0.85
    linear 2.0 xpos 1.2 ypos 0.85
    linear 2.0 zoom 0.01

transform move_in_enter:
    xpos 0.1
    ypos 0.9
    xzoom -1.0
    linear 2 xpos 0.65 ypos 0.5


define floppa = Character("Floppa", color="#ec7e17")
define unknownfloppa = Character("???", color="#ec7e17")
define bananacat = Character("Banana Cat", color="#818821")
define unknownbanana = Character("???", color="#818821")
define spincat = Character("Spin Cat", color="#ffffff")
define unknownSpincat = Character("???", color="#ffffff")

image floppa_idle = "images/floppa/idle.png"
image floppa_talk = "images/floppa/talk.png"
image spincat_idle = "images/spincat/idle.png"


define spincat_sound_normal = "audio/spincat/normal.mp3"
define banana_sound_normal = "audio/banana/normal.mp3"
define alarm = "audio/alarm.mp3"
define ambientIdle = "audio/pvz.mp3"
define click = "audio/pop_short.mp3"

default spincatController = AnimationController("images/spincat/spin", 59, 0.033)
default bananaController = AnimationController("images/bananacat", 119, 0.033)

image bg bmstu = "images/backgrounds/bmstu.jpg"
image bg house = "images/backgrounds/house.jpg"
image bg enter = "images/backgrounds/enter.png"
image bg enter_2 = "images/backgrounds/enter_2.png"
image bg coffee = "images/backgrounds/coffee.png"
image bg gool = "images/backgrounds/gool.png"
image bg black = "images/backgrounds/black.png"

image spincat_animation:
    xalign 0.5
    yalign 0.5
    "[spincatController.current_frame]"
    function spincatController.next_frame
    pause spincatController.interval
    repeat

image banana_animation:
    xalign 0.5
    yalign 0.5
    "[bananaController.current_frame]"
    function bananaController.next_frame
    pause bananaController.interval
    repeat


label start:
    jump morning

label morning:
    scene bg black
    unknownfloppa "День первый."
    pause(1)
    unknownSpincat "Ох... Как же болит голова."
    play sound click
    unknownSpincat "Хорошо вчера день провёл. Может поспать ещё пять минуточек?"
    menu:

        "Поспать":
            unknownSpincat "Ну посплю ещё немного. Что может случиться?"
            $ firstdayfail = 1
            jump latefirstday

        "Встать":
            unknownSpincat "Лучше встану. А то ещё и опоздаю. В первый же день."
            $ firstdayfail = 0
            jump firstday

label latefirstday:
    play sound alarm loop
    unknownSpincat "..."
    stop sound
    unknownSpincat "ААААА"
    show bg house
    with Dissolve(.5)
    play music ambientIdle loop
    show spincat_idle:
        xalign 0.85
        yalign 0.85
    play sound click
    spincat "Уже 8 утра?! Я точно не успею! Надо торопиться."
    play sound click
    spincat "Погнали!"
    play sound spincat_sound_normal loop
    hide spincat_idle
    show spincat_animation at move_to_door
    pause(4)
    stop sound
    with fade
    jump firstdayenterlater
    


label firstday:
    show bg house
    with Dissolve(.5)
    spincat "Ну что народ погнали!"
    play sound spincat_sound_normal loop
    hide spincat_idle
    show spincat_animation at move_to_door
    pause(4)
    stop sound
    with fade
    jump firstdayenter


label firstdayenterlater:
    scene bg black
    scene bg bmstu
    with Dissolve(.5)
    show spincat_idle:
        xalign 0.85
        yalign 0.85
    spincat "Блин, опоздал. Я же не знаю куда идти..."
    play sound click
    spincat "Привет. Как звать?"
    play sound click
    show floppa_idle:
        xalign 0.25
        yalign 0.85
        zoom 0.5
    floppa "Привет. Я Шлёпа. Можешь звать Бывалым."
    play sound click
    floppa "Но это ты зря пришёл. Можешь уходить домой."
    play sound click
    spincat "Это ещё почему?"
    play sound click
    floppa "У нас первой парой физкультура. Самый важный предмет в нашем университете!"
    play sound click
    floppa "Тебя всё равно не пустят. Приходи в другой раз."
    play sound click
    spincat "Погоди, а что насчёт тебя? Почему ты не пошёл?"
    play sound click
    floppa "Так я из академа пришёл. У меня перезачёт."
    play sound click
    spincat "А, ну ладно. Давай тогда до завтра."
    play sound click
    floppa "Рад знакомству. Пока!"
    play sound click
    hide spincat_idle
    play sound spincat_sound_normal loop
    show spincat_animation at move_out_university
    pause(2)
    hide spincat_animation
    hide floppa_idle
    jump secondday



label firstdayenter:
    scene bg bmstu
    with Dissolve(.5)
    show spincat_idle:
        xalign 0.85
        yalign 0.85
    spincat "Ох, как много людей! Надо бы с кем-то познакомиться!"
    play sound click
    spincat "Привет. Как звать?"
    play sound click
    show floppa_idle:
        xalign 0.25
        yalign 0.85
        zoom 0.5
    floppa "Привет. Я Шлёпа. Можешь звать Бывалым."
    play sound click
    spincat "Рад знакомству. Я спинкэт. Пойдёшь на физру"
    play sound click
    floppa "Не, у меня она уже закрыта. Так что давай без меня."
    play sound click
    spincat "А, ну ладно. Давай тогда до завтра."
    play sound click
    floppa "Удачи"
    play sound click
    hide spincat_idle
    play sound spincat_sound_normal loop
    show spincat_animation at move_out_university
    pause(2)
    hide spincat_animation
    hide floppa_idle
    jump secondday

label secondday:
    scene bg black
    unknownfloppa "День второй."
    pause(1)
    show bg enter
    with Dissolve(.5)
    show spincat_idle:
        xalign 0.85
        yalign 0.85
    if firstdayfail == 1:
        play sound click
        spincat "... неудобно конечно вчера получилось"
        play sound click
        spincat "Ну ладно, надеюсь последствий не будет"
    else:
        play sound click
        spincat "Классно вчера поиграли"
        play sound click
        spincat "Пойти в группу по игре в нарды было лучшим решением"
        
    play sound click
    spincat "Сегодня попробую войти через другой вход."
    show bg enter_2
    with Dissolve(1)
    play sound click
    spincat "С каких пор проверяют рюкзаки на входе?"
    play sound click
    spincat "И чем им так планшет на авроре не угодил?"
    play sound click
    spincat "Ну неважно"
    unknownbanana "С дороги!!!"
    play sound banana_sound_normal loop
    show banana_animation at move_in_enter
    pause(2)
    stop sound
    hide banana_animation
    play sound click
    spincat "Ну дурак. Всё настроение испортил"
    play sound click
    spincat "Может пойти попить кофе"
    menu:
        "Пойти за кофе":
            play sound click
            spincat "А что, почему нет?"
            play sound click
            spincat "Как говорится"
            play sound click
            spincat "Лучше посрать и опоздать"
            play sound click
            spincat "чем прийти вовремя и обосраться"
            play sound click
            spincat "Да и кофе защищает от альцгеймера"
            play sound click
            scene bg coffee
            with Dissolve(.5)
            spincat "Кофе, хороший кофе это очень вкусно."
            play sound click
            spincat "На самом деле рецепт простой — много шотов, мало пенки"
            play sound click

            hide spincat_idle

            $ seconddayfail = 1
            jump thirdday

        "Бежать на пару":
            play sound click
            spincat "Не, лучше пока не опаздывать."
            play sound click
            spincat "А куда мне идти? Забыл что-то"
            play sound click
            spincat "А, вспомнил! Видимо стоит носить кофе с собой"

            hide spincat_idle

            $ seconddayfail = 0
            jump thirdday



label thirdday:
    scene bg black
    unknownfloppa "День третий. Финал"
    pause(1)
    if seconddayfail + firstdayfail == 2:
        unknownfloppa "Спинкэт был слишком безрасудным"
        play sound click
        unknownfloppa "По итогу его отчислили"
        play sound click
    
    if seconddayfail + firstdayfail == 1:
        unknownfloppa "Спинкэт конечно накосячил, но всё нормально"
        play sound click
        unknownfloppa "А вот бананчик с гнильцой оказался. Забрали бедного..."
        play sound click
    
    if seconddayfail + firstdayfail == 0:
        unknownfloppa "Спинкэт конечно молодец"
        play sound click
        unknownfloppa "В конце недели решили сходить в антикафе"
        play sound click
        scene bg gool
        show spincat_idle:
            xalign 0.65
            yalign 0.45
        show floppa_idle:
            xalign 0.25
            yalign 0.45
            zoom 0.5
        spincat "БИТОООООО!"
        play sound click
        floppa "Ты дурак? Мы в футбол играем."
    

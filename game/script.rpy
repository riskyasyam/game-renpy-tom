﻿init python:
    # Tambahkan keymap ESC untuk memanggil custom menu
    config.keymap['toggle_pause'] = ['K_ESCAPE']

label _pause_menu:
    show screen pause
    $ ui.interact()
    return

define e = Character('Raka', color="#ffff")
define pakTua = Character("Tetua Desa", color="#ffff")

label start:
    call level_1 from _call_level_1
    call level_2 from _call_level_2
    call level_3 from _call_level_3
    call level_4 from _call_level_4

# Kamu dapat taruh script game mu di file ini.



# # Menghentikan musik
# stop music

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg_lvl1_1 = "images/bg_lvl1_1.png"
image bg_lvl1_2 = "images/bg_lvl1_2.png"
image bg_lvl1_3 = "images/bg_lvl1_3.png"
image bg_lvl1_4 = "images/bg_lvl1_4.png"
image bg_lvl1_5 = "images/bg_lvl1_5.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Raka', color="#c8ffc8")

# Game dimulai disini.
label start:
    # Memulai musik latar
    play music "audio/music/sound.mp3" loop
    
    scene bg_lvl1_1 with dissolve
    "*Suara burung"
    "Pagi yang indah untuk memulai hari di jalan Mastrip."

    scene bg_lvl1_2 with dissolve
    e "Oh, ini jalan mastrip... Ramai juga ya disini.."

    return

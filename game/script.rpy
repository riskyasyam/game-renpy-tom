# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg_lvl1_1 = "images/bg_lvl1_1.png"
image bg_lvl1_2 = "images/bg_lvl1_2.png"
image bg_lvl1_3 = "images/bg_lvl1_3.png"
image bg_lvl1_4 = "images/bg_lvl1_4.png"
image bg_lvl1_5 = "images/bg_lvl1_5.png"
image bg_lvl1_6 = "images/bg_lvl1_6.png"
image bg_lvl1_7 = "images/bg_lvl1_7.png"
image bg_lvl1_8 = "images/bg_lvl1_8.png"
image bg_lvl1_9 = "images/bg_lvl1_9.png"


# Deklarasikan karakter yang digunakan di game.
define e = Character('Raka', color="#ffff")
define pakTua = Character("Tetua Desa", color="#ffff")

screen bersambung_screen:
    # Overlay gelap
    add "images/black_transparent.png"

    # Teks di tengah layar
    text "Bersambung" size 60 color "#EABC67" xalign 0.5 yalign 0.4 font "fonts/Stevens-Titling-W01-SableBrush.ttf"

    # Tombol di bawah teks
    textbutton "Selanjutnya":
        action Return()  # Fungsi untuk kembali ke script setelah screen selesai
        xalign 0.5
        yalign 0.5
        background Frame("#ECDEBF", 15, 15)
        hover_background Frame("#B4A075", 15, 15)
        padding (10, 20)
        text_size 30


# Game dimulai disini.
label start:
    stop music
    # Memulai musik latar
    
    scene bg_lvl1_1 with dissolve
    play music "audio/music/bg_sound.mp3"
    play sound "audio/bird_song.mp3"
    "*Suara burung"
    "Pagi yang indah untuk memulai hari di jalan Mastrip."

    scene bg_lvl1_2 with dissolve
    e "La la la la la"
    e "Oh, ini jalan mastrip... Ramai juga ya disini.."
    stop sound

    scene bg_lvl1_3 with dissolve
    e "A-apa ini? Kenapa tanganku muncul cahaya aneh berwarna biru"

    scene bg_lvl1_4 with dissolve
    e "Apa yang terjadi..!!"

    scene bg_lvl1_5
    "Raka terlempar ke masa lalu dimana dia melihat banyak sekali orang orang berpakaian seperti tentara lama dan juga bangunan yang kuno"
    e "Dimana ini? Kenapa aku ada disini? Apa yang terjadi denganku..."
    e "Kenapa semuanya berpakaian seperti tentara???!!!"

    scene bg_lvl1_6
    "Raka terlihat bingung dengan situasi yang ada disini"
    e "Apakah ini di masa lalu?? Semuanya terlihat sangat kuno"
    pakTua "Hei nak.."

    scene bg_lvl1_7
    "Ada seorang bapak tetua di desa itu yang kemudian memanggil Raka yang sedang kebingungan"
    pakTua "Hei nak, saya seperti tidak asing melihat wajahmu ini, sepertinya saya tau kamu. Kemari ikutin saya"

    scene bg_lvl1_8
    pakTua "Nak, kamu persis seperti ramalan pada desa ini. Kamu adalah orang yang dikirim untuk menyelamatkan desa ini"
    e "Maksudnya pakk??"
    pakTua "Desa ini sedang dalam bahaya. Banyak penjajah yang membunuh warga sini"
    e "Penjajah??"
    pakTua "Iya nak. Kamu bisa bantu kami?"
    e "Emm saya kurang tau kondisinya, tetapi karena keliatannya saya adalah orang yang bapak maksud, saya siap"

    scene bg_lvl1_9
    "Pasukan tentara tim Raka mulai mempersiapkan diri untuk memasuki hutan belantara mastrip untuk melawan penjajah"

    call screen bersambung_screen
    
    return

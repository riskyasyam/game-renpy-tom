image bg_lvl1_1 = "images/bg_lvl1_1.png"
image bg_lvl1_2 = "images/bg_lvl1_2.png"
image bg_lvl1_3 = "images/bg_lvl1_3.png"
image bg_lvl1_4 = "images/bg_lvl1_4.png"
image bg_lvl1_5 = "images/bg_lvl1_5.png"
image bg_lvl1_6 = "images/bg_lvl1_6.png"
image bg_lvl1_7 = "images/bg_lvl1_7.png"
image bg_lvl1_8 = "images/bg_lvl1_8.png"
image bg_lvl1_9 = "images/bg_lvl1_9.png"

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


label level_1:
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

    #Pilihan ikut atau tidak
    menu:
        "Ikut Perang":
            jump ikut_perang
        "Tidak Ikut Perang":
            jump tidak_ikut_perang

    label ikut_perang:   
        scene bg_lvl1_9
        "Pasukan tentara tim Raka mulai mempersiapkan diri untuk memasuki hutan belantara Mastrip untuk melawan penjajah"
        e "Saya akan membantu desa ini. Apa yang harus saya lakukan?"
        pakTua "Persiapkan dirimu, kita harus segera bergerak!"
        # Tambahkan lanjutan cerita di sini
        call screen bersambung_screen
        return

    label tidak_ikut_perang:
        scene bg_lvl1_6
        "Raka memutuskan untuk tidak ikut perang, tetapi ia tetap memutuskan untuk bertahan di desa dan membantu dengan cara lain."
        e "Saya tidak yakin bisa ikut perang, Pak. Tapi mungkin ada hal lain yang bisa saya lakukan untuk membantu?"
        pakTua "Baiklah, nak. Kalau begitu, kamu bisa membantu kami menjaga desa ini tetap aman sementara kami melawan penjajah."
        
        # Narasi untuk menghubungkan kembali ke jalan utama
        "Beberapa hari berlalu, dan meskipun Raka tidak ikut ke medan perang, situasi di desa memaksa dia untuk mengambil keputusan besar."
        e "Sepertinya, cepat atau lambat, saya harus menghadapi para penjajah ini juga."
        
        # Lanjutkan ke jalan utama
        jump jalan_utama

    label jalan_utama:
        scene bg_lvl1_9
        "Raka akhirnya bergabung kembali de ngan pasukan utama untuk melawan penjajah di hutan belantara Mastrip."
        e "Ini saatnya. Saya tidak bisa lari lagi dari tanggung jawab ini."
        pakTua "Bagus, nak. Denganmu di sini, saya yakin kita bisa mengalahkan mereka!"
        # Tambahkan cerita lanjutan di sini
        return
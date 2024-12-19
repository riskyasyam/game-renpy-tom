image bg_lvl2_1 = "images/bg_level_2/1_hutan_terlarang_1.png"
image bg_lvl2_2 = "images/bg_level_2/2_jebakan_hutan.png"
image bg_lvl2_3 = "images/bg_level_2/3_artefak_hutan.png"
image bg_lvl2_4 = "images/bg_level_2/4_mata_mata.png"
image bg_lvl2_5 = "images/bg_level_2/5_hewan_endemik.png"
image bg_lvl2_6 = "images/bg_level_2/5_hewan_endemik_2.png"
image bg_lvl2_7 = "images/bg_level_2/6_akhir_dari_hutan.png"
# image bg_lvl2_8 = "images/bg_lvl1_8.png"
# image bg_lvl2_9 = "images/bg_lvl1_9.png"
# image bg_lvl2_raka_mencari = "images/bg_lvl1_raka_mencari.png"
# image bg_lvl2_semak = "images/bg_lvl1_semak.png"
# image bg_lvl2_nolak = "images/bg_lvl1_nolak.jpg"
# image bg_lvl2_desa_hancur = "images/bg_lvl1_desa_hancur.jpg"

define e = Character('Raka', color="#ffff")
# define pakTua = Character("Tetua Desa", color="#ffff")

screen bersambung_screen:
    add "images/bg_level_2/6_akhir_dari_hutan.png"

    text "Bersambung" size 60 color "#EABC67" xpos 0.5 ypos 0.4 font "fonts/Stevens-Titling-W01-SableBrush.ttf" anchor (0.5, 0.5)

    textbutton "Selanjutnya":
        action Return()
        xpos 0.5
        ypos 0.6
        background Frame("#ECDEBF", 15, 15)
        hover_background Frame("#B4A075", 15, 15)
        padding (10, 20)
        text_size 30
        anchor (0.5, 0.5)

label level_2:
    stop music fadeout 2.0

    # Memulai scene level 2 dengan musik latar
    scene bg_lvl2_1 with dissolve
    play music "audio/music/bgm_level2.mp3" loop
    play sound "audio/music/walk_sound_effect.mp3"
    "Raka, memasuki hutan yang dipenuhi pepohonan tinggi dengan akar menjalar. Cahaya matahari yang menembus dedaunan menciptakan pola bayangan mistis di tanah."

    e "Ini dia... Hutan Mastrip. Katanya penuh teka-teki dan jebakan. Semoga aku bisa melewatinya dengan selamat."

    # Pilihan pertama
    menu:
        "Berjalan perlahan sambil mengamati sekitar":
            "Raka melangkah perlahan, mengamati setiap detail di sekitarnya untuk menghindari jebakan atau bahaya tersembunyi."
            e "Aku harus berhati-hati... tempat seperti ini penuh dengan misteri."
            jump jebakan
        "Melangkah lebih cepat agar segera keluar":
            "Raka mempercepat langkahnya, yakin pada kemampuannya untuk bereaksi cepat terhadap bahaya yang mungkin muncul."
            e "Semakin cepat aku bergerak, semakin cepat aku bisa keluar dari tempat ini."
            jump jebakan

label jebakan:
    stop sound fadeout 1.0
    scene bg_lvl2_2 with dissolve
    "Raka berhenti mendadak ketika melihat sesuatu yang mencurigakan di tanah. Ternyata itu adalah jebakan yang tersembunyi di bawah dedaunan."
    e "Hah, jebakan seperti ini pasti dibuat untuk menghalangi siapa pun yang masuk ke hutan ini. Untung saja aku berhati-hati."
    e "Aku harus mencari jalan lain."

    jump simbol_rahasia

label simbol_rahasia:
    scene bg_lvl2_3 with dissolve
    "Di tengah perjalanan, Raka menemukan batu besar dengan ukiran simbol yang terlihat seperti petunjuk rahasia."
    e "Simbol ini... apakah ini semacam petunjuk? Sepertinya ini mengarah ke sesuatu yang penting."

    menu:
        "Mencatat simbol ke dalam buku catatan":
            "Raka mencatat simbol tersebut dengan hati-hati di buku catatannya untuk digunakan nanti."
            e "Aku tidak tahu kapan ini akan berguna, tapi lebih baik aku mencatatnya."
            jump harimau_penjaga
        "Mencoba memahami simbol langsung di tempat":
            "Raka mencoba memahami arti simbol tersebut dengan mengamati setiap detailnya."
            e "Ini terlihat seperti petunjuk untuk sesuatu... mungkin ada kaitannya dengan penjaga hutan ini."
            jump harimau_penjaga

label harimau_penjaga:
    scene bg_lvl2_4 with dissolve
    "Musuh mengetahui keberadaan Raka dan mulai mendekatinya untuk menyergap. Namun, sebelum mereka berhasil, seekor harimau besar muncul dari balik pepohonan."
    scene bg_lvl2_5 with dissolve
    "Harimau tersebut mengusir musuh dengan auman yang keras, membuat mereka melarikan diri dengan ketakutan."
    e "Harimau ini... dia seperti penjaga hutan. Apakah dia juga penjaga simbol tadi?"

    menu:
        "Mengikuti harimau ke arah tertentu":
            "Raka memutuskan untuk mengikuti harimau, yang tampaknya mengarah ke tempat yang lebih dalam di hutan."
            e "Mungkin harimau ini tahu sesuatu yang penting... Aku harus mengikutinya."
            jump keluar_hutan
        "Berhenti dan menyusun rencana baru":
            "Raka memilih untuk berhenti sejenak, menyusun strategi sebelum melanjutkan perjalanan."
            e "Aku harus berhati-hati. Hutan ini penuh misteri, dan aku tidak boleh gegabah."
            jump keluar_hutan

label keluar_hutan:
    scene bg_lvl2_7 with dissolve
    "Setelah mengikuti petunjuk dan menghadapi berbagai tantangan, Raka akhirnya berhasil keluar dari Hutan Mastrip."
    e "Aku berhasil... tapi ini baru awal dari perjalanan. Aku harus melanjutkan perjuangan untuk melawan penjajah."
    call screen bersambung_screen
    return
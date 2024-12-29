# Definisi gambar dan ikon
image bg_lvl4_1 = "images/bg_level_4/1_opening_penyergapan.png"
image bg_lvl4_2 = "images/bg_level_4/2_penyusupan_gudang_senjata.png"
image bg_lvl4_3 = "images/bg_level_4/3_peledakan_gudang_senjata.jpg"
image bg_lvl4_4 = "images/bg_level_4/4_penyergapan_dimulai.jpg"
image bg_lvl4_5 = "images/bg_level_4/5_peperangan_malam.jpg"
image bg_lvl4_6 = "images/bg_level_4/6_perang_tengah_malam.jpg"
image bg_lvl4_7 = "images/bg_level_4/7_van_der_wall.jpg"
image bg_lvl4_8 = "images/bg_level_4/8_kemerdekaan.jpg"

image icon_gudang = "images/icons/gudang.png"
image icon_battle = "images/icons/battle.png"

# Definisi karakter
define e = Character('Raka', color="#ffff")
define narrator = Character("Narrator", color="#EABC67")

# Variabel poin untuk interaksi lebih lanjut
default courage_points = 0

label level_4:
    stop music fadeout 2.0

    # Opening scene dengan narasi
    scene bg_lvl4_1 with fade
    play music "audio/music/bgm_level2.mp3" loop
    play sound "audio/music/walk_sound_effect.mp3"
    narrator "Raka berhasil menyelamatkan sandera penting dari cengkeraman penjajah. Namun, ini baru permulaan. Dengan rencana matang dan persatuan warga, malam ini menjadi saksi sejarah perlawanan terhadap penjajahan."

    # Menu awal untuk meningkatkan interaksi
    menu:
        "Bicara dengan pasukan":
            e "Kawan-kawan, kita telah bersatu demi malam ini. Mari kita buktikan keberanian kita!"
            $ courage_points += 1
        "Mengatur strategi":
            e "Strategi kita harus tepat. Pastikan semua orang tahu peran mereka!"
            $ courage_points += 2

    jump penyergapan

label penyergapan:
    stop sound fadeout 1.0
    scene bg_lvl4_4 with dissolve
    e "Kawan-kawan, malam ini adalah malam kita! Kita akan menunjukkan bahwa keberanian dan persatuan kita mampu mengalahkan mereka."
    e "Tetap maju! Jangan biarkan mereka mengintimidasi kita!"

    menu:
        "Memimpin penyergapan":
            e "Aku akan berada di garis depan. Ikuti aku!"
            $ courage_points += 3
        "Memberi instruksi dari belakang":
            e "Kalian maju dulu, aku akan memantau dari sini."
            $ courage_points += 1

    jump penyusupan_gudang_senjata

label penyusupan_gudang_senjata:
    scene bg_lvl4_2 with dissolve
    e "Kawan-kawan, kita telah menemukan gudang senjata yang tersembunyi di sekitar kita."

    menu:
        "Mengambil senjata":
            e "Aku akan mengambil senjata ini. Pastikan semua orang tahu peran mereka!"
            $ courage_points += 2
        "Memerintahkan pasukan lain":
            e "Kalian, pastikan semua berjalan lancar. Aku akan melindungi dari jarak jauh."
            $ courage_points += 1

    jump peledakan_gudang_senjata

label peledakan_gudang_senjata:
    scene bg_lvl4_3 with dissolve
    e "Inilah saatnya! Kita harus meledakkan gudang senjata ini agar mereka tidak bisa menggunakannya lagi!"

    menu:
        "Menyalakan sumbu peledak":
            e "Aku akan menyalakan sumbu. Ayo, mundur dengan cepat!"
            $ courage_points += 3
        "Memerintahkan pasukan lain":
            e "Kalian, pastikan semua berjalan lancar. Aku akan melindungi dari jarak jauh."
            $ courage_points += 2

    jump perang_malam

label perang_malam:
    scene bg_lvl4_5 with fade
    e "Pertempuran sudah dimulai. Ayo, kita harus memenangkan ini untuk masa depan kita!"

    # Menambahkan narasi sesuai poin keberanian
    if courage_points >= 7:
        narrator "Raka memimpin dengan semangat luar biasa, meningkatkan moral semua pasukan."
    else:
        narrator "Pasukan tetap berjuang keras meskipun situasi mulai menantang."

    jump perang_tengah_malam

label perang_tengah_malam:
    scene bg_lvl4_6 with dissolve
    e "Malam semakin larut, tapi semangat kita tak boleh padam. Kita harus terus berjuang!"

    menu:
        "Menghadapi langsung Van Der Wall":
            e "Aku akan menghadapi dia sendiri. Ini saatnya membuktikan keberanian kita."
            $ courage_points += 5
        "Menginstruksikan serangan serentak":
            e "Serang bersamaan! Jangan beri dia kesempatan menyerang balik!"
            $ courage_points += 3

    jump van_der_wall

label van_der_wall:
    scene bg_lvl4_7 with fade
    e "Ini adalah saat yang kita tunggu-tunggu. Mari kita tunjukkan kepada Van Der Wall bahwa kita tidak bisa ditundukkan!"

    menu:
        "Menghadapi langsung Van Der Wall":
            e "Aku akan menghadapi dia sendiri. Ini saatnya membuktikan keberanian kita."
            $ courage_points += 5
        "Menginstruksikan serangan serentak":
            e "Serang bersamaan! Jangan beri dia kesempatan menyerang balik!"
            $ courage_points += 3

    jump kemerdekaan

label kemerdekaan:
    scene bg_lvl4_8 with fade
    if courage_points >= 10:
        narrator "Akhirnya, perjuangan panjang ini berakhir dengan kemenangan besar. Keberanian luar biasa Raka dan pasukan membuat perlawanan ini menjadi sejarah."
    else:
        narrator "Kemerdekaan tercapai, tetapi perjuangan ini mengingatkan bahwa persatuan dan keberanian selalu dibutuhkan."

    return

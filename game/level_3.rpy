image bg_lvl3_1 = "images/bg_lvl3_1.png"
image bg_lvl3_2 = "images/bg_lvl3_2.png"
image bg_lvl3_3 = "images/bg_lvl3_3.png"
image bg_lvl3_4 = "images/bg_lvl3_4.png"
image bg_lvl3_5 = "images/bg_lvl3_5.png"
image bg_lvl3_6 = "images/bg_lvl3_6.png"

define e = Character('Raka', color="#ffff")

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


label level_3:
    scene bg_lvl3_1
    e "Bangunan ini... mereka pasti sudah lama di sini. Tidak mungkin mereka bisa membangun markas seperti ini tanpa perencanaan matang. Tapi bagaimana bisa kami tak menyadari keberadaan mereka selama ini? Apa yang mereka sembunyikan di dalam sana?"
    
    "Raka menatap bangunan besar yang sebagian tertutup pepohonan lebat. Lampu-lampu penjagaan menyapu area sekitar dengan intensitas tinggi, membuatnya harus lebih hati-hati."
    
    menu:
        "Mengamati area sekitar":
            e "Aku harus mempelajari pola penjagaan mereka terlebih dahulu. Jika aku terburu-buru, aku hanya akan masuk ke jebakan mereka."
            "Raka berjongkok di balik semak-semak, memperhatikan gerak-gerik para penjaga. Ia mencatat waktu pergantian patroli dan arah lampu sorot."
        
        "Langsung menyelinap masuk":
            e "Tidak ada waktu untuk menganalisa lebih jauh. Aku harus bertindak cepat sebelum mereka menyadari keberadaanku."
            "Dengan napas tertahan, Raka melangkah perlahan di antara bayangan pepohonan, berharap tidak tertangkap basah oleh penjaga."

    scene bg_lvl3_2
    "Setelah memastikan area aman, Raka melanjutkan langkahnya menuju pintu samping markas yang tampaknya lebih jarang dijaga."
    
    menu:
        "Mencari jalur alternatif":
            e "Pintu ini terlalu mencolok. Aku yakin mereka memiliki jalur lain, mungkin melalui ventilasi atau saluran bawah tanah."
            "Raka berjalan memutar, menemukan sebuah lubang ventilasi yang cukup besar untuk dilewati."
        
        "Memaksa masuk melalui pintu":
            e "Ini mungkin berisiko, tapi aku tidak punya banyak waktu untuk mencari jalan lain."
            "Raka mengeluarkan alat pembuka kunci dari sakunya dan mulai bekerja membuka pintu."

    scene bg_lvl3_3
    e "Langkah demi langkah… jangan sampai mereka mendengar. Tempat ini lebih besar dari yang kuduga. Pengawal di setiap sudut. Tapi aku sudah sejauh ini. Tak ada jalan untuk mundur."
    
    "Raka menemukan sebuah ruangan yang penuh dengan dokumen dan peta. Ia menyadari bahwa ruangan ini mungkin menyimpan informasi penting."
    
    menu:
        "Mencari dokumen penting":
            e "Jika aku bisa menemukan bukti keberadaan mereka dan rencana mereka, ini akan sangat membantu misi kami."
            "Raka memeriksa meja dan rak, menemukan peta besar dengan catatan yang menunjukkan lokasi-lokasi strategis mereka."
        
        "Mengabaikan dan melanjutkan ke area utama":
            e "Aku tidak punya waktu untuk ini. Fokus utamaku adalah menyelamatkan para tahanan."
            "Raka meninggalkan ruangan dan menuju koridor utama."

    scene bg_lvl3_4
    "Alarm berbunyi nyaring, asap memenuhi beberapa ruangan. Para tentara musuh berlarian, mencoba mengendalikan situasi. Raka bersembunyi di balik peti besar, menunggu momen yang tepat untuk bergerak."

    e "Alarm... seseorang pasti sudah menyadari keberadaanku. Aku harus cepat."
    
    menu:
        "Mengalihkan perhatian penjaga":
            e "Aku bisa menciptakan gangguan untuk menarik perhatian mereka ke arah lain."
            "Raka menyalakan alarm palsu di ruangan sebelah, membuat para penjaga berlari ke arah suara tersebut."
        
        "Melanjutkan perjalanan tanpa gangguan":
            e "Aku tidak bisa mengambil risiko mereka kembali ke sini. Aku harus tetap diam dan bergerak perlahan."
            "Raka tetap bersembunyi hingga penjaga di dekatnya pergi, lalu melanjutkan langkahnya."

    scene bg_lvl3_5
    "Raka akhirnya menemukan ruang tahanan. Beberapa orang terlihat di balik jeruji, memandangnya dengan harapan."
    
    e "Aku di sini untuk menyelamatkan kalian. Tapi kita harus cepat. Mereka pasti sudah curiga dengan ledakan di atas. Ikuti aku, tetap diam, dan jangan berhenti apa pun yang terjadi."
    
    "Raka membuka kunci sel menggunakan alatnya, dan para tahanan mulai bergerak mengikutinya."
    
    scene bg_lvl3_6
    "Keluar dari pagar, Raka memimpin para tahanan melalui hutan gelap. Namun, suara langkah kaki pasukan musuh terdengar semakin dekat."

    e "Kita sudah keluar dari pagar, tapi ini belum selesai. Mereka pasti mengirim pasukan untuk mengejar kita. Kita harus terus bergerak."
    
    menu:
        "Membagi kelompok untuk mengurangi risiko":
            e "Kita terlalu banyak untuk bergerak bersama. Kita akan lebih sulit ditemukan jika terpisah."
            "Raka memberikan instruksi untuk membagi kelompok dan menentukan titik pertemuan."
        
        "Tetap bersama untuk melindungi semua orang":
            e "Kita harus tetap bersama. Jika terpisah, risiko tertangkap jauh lebih besar."
            "Raka memimpin semua orang melewati jalur tersembunyi, menjaga agar kelompok tetap bersatu."

    call screen bersambung_screen

    return

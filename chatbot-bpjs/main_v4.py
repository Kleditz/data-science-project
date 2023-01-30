###--------------------------------------------------------------------------------###
# Library

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import User
from keys import token
from telegram.ext import *
from telebot import *

###--------------------------------------------------------------------------------###

bot = Bot(token=token)
dp = Dispatcher(bot)

'''
Contoh penggunaan inline dan outline keyboard pada lib tele-py-bot dan telebot

# Inline keyboard -> /random
button1 = InlineKeyboardButton(text="button1", callback_data="apaitu")
button2 = InlineKeyboardButton(text="button2", callback_data="caritauro")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

# Keyboard
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Hello!", "LinkedIn")

# Inline keyboard handler -> /random
@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)

# Keyboard handler
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im Kadek Aditya Premaswara, Please follow my LinkedIN", reply_markup=keyboard1)

# Query for /random -> Inline Keyboard
@dp.callback_query_handler(text=["apaitu", "caritauro"])
async def random_value(call: types.CallbackQuery):
    if call.data == "apaitu":
        await call.message.answer(str("BPJS Kesehatan untuk Badan Usaha adalah layanan untuk..."))
    if call.data == "caritauro":
        await call.message.answer(str("Baik anda akan diminta untuk memilih cabang BPJS di kabupaten terdekat Badan Usaha anda..."))
    await call.answer()

# Keyboard message handler
@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Hello!':
        await message.reply("Hi! How are you?")
    elif message.text == 'LinkedIn':
        await message.reply("https://www.linkedin.com/in/kadek-aditya-premaswara/")
    else:
        await message.reply(f"Your message is: {message.text}")
'''
###-------------------------------------------------###
# Booting bot
print('Project Akhir Nadya|BPJS Kesehatan')
print('memulai chatbot...')
print('loading python, kleditz_venv...')
print('chatbot status :: LAUNCHED')


###--------------------------------------------------###
# Keyboard
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("MULAI")

# Commands /start /help /etc
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Selamat Datang!, sebelum kita memulai. mohon pilih:", reply_markup=keyboard1)
@dp.message_handler(commands=['help'])
async def helpme(message: types.Message):
    if message.text.lower() == "/help" or "help":
        await message.reply("gunakan ' /start ' untuk memulai chatbot...")

# Keyboard response
@dp.message_handler()
async def keyboard1_answer(message: types.Message):
    if message.text == 'MULAI':
        name = message.from_user.first_name
        await message.reply("Halo " + (name) + ". Bagaimana kabar anda?")
        await message.answer("Layanan ini adalah chatbot/layanan chat otomatis dari BPJS Kesehatan untuk Badan Usaha yang ditujukan memberikan informasi-informasi yang dapat membantu bapak/ibu.")
        await message.answer("Ada yang bisa saya bantu ?", reply_markup=keyboard_inline1)
    # elif message.text == 'EN':
    #     name = message.from_user.first_name
    #     await message.reply("Hello " + (name) + ". How are you?")
    #     await message.answer("This service is a chatbot/automated chat service from BPJS Kesehatan for Business Entities aimed at providing information that can help you.")
    #     await message.answer("May I help you ?", reply_markup=keyboard_inline2)
    else:
        await message.reply(f"Your message is: {message.text.lower()}. I don't have idea about that :(" "\n"
        "Please use /help instead (with '/')" "\n"
        "\n"
        f"Pesan anda: {message.text.lower()}. Maaf saya tidak mengerti :(" "\n"
        "Mohon gunakan /help (dengan '/')")

#Keyboard Inline 1
button1 = InlineKeyboardButton(text="Registrasi Badan Usaha", callback_data="aa")
button2 = InlineKeyboardButton(text="Iuran dan Denda", callback_data="bb")
button3 = InlineKeyboardButton(text="Mutasi Data", callback_data="cc")
button4 = InlineKeyboardButton(text="Perubahan Data", callback_data="dd")
button5 = InlineKeyboardButton(text="Penonaktifan VA BU", callback_data="ee")
button6 = InlineKeyboardButton(text="Edabu", callback_data="ff")
button7 = InlineKeyboardButton(text="Info JKN", callback_data="gg")
keyboard_inline1 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(button7)

#Query Keyboard 1
@dp.callback_query_handler(text=["aa", "bb", "cc", "dd", "ee", "ff", "gg"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "aa":
        await call.message.answer(str("Menampilkan cara Registrasi Badan Usaha:"), reply_markup=keyboard_inline2)
    if call.data == "bb":
        await call.message.answer(str("Menampilkan Informasi seputar Iuran dan Denda:"), reply_markup=keyboard_inline3)
    if call.data == "cc":
        await call.message.answer(str("Menampilkan cara Mutasi Data:"), reply_markup=keyboard_inline4)
    if call.data == "dd":
        await call.message.answer(str("Menampilkan cara Perubahan Data:"), reply_markup=keyboard_inline5)
    if call.data == "ee":
        await call.message.answer(str("Menampilkan cara Penonaktifan VA BU:"), reply_markup=keyboard_inline6)
    if call.data == "ff":
        await call.message.answer(str("Menampilkan Informasi seputar Edabu:"), reply_markup=keyboard_inline7)
    if call.data == "gg":
        await call.message.answer(str("Menampilkan Informasi seputar JKN:"), reply_markup=keyboard_inline8)

    await call.answer()

#Keyboard Inline Regis BU
button1 = InlineKeyboardButton(text="a. Syarat Registrasi BU", callback_data="aa1")
button2 = InlineKeyboardButton(text="b.	Penerbitan Sertifikat", callback_data="aa2")
button3 = InlineKeyboardButton(text="c.	Penerbitan Surat Keterangan", callback_data="aa3")
keyboard_inline2 = InlineKeyboardMarkup().add(button1).add(button2).add(button3)

#Keyboard Inline IuranDenda
button1 = InlineKeyboardButton(text="a. Informasi Tagihan Iuran", callback_data="bb1")
button2 = InlineKeyboardButton(text="b.	Informasi Tunggakan", callback_data="bb2")
button3 = InlineKeyboardButton(text="c.	Rekonsiliasi Data Peserta & Iuran", callback_data="bb3")
button4 = InlineKeyboardButton(text="d.	Denda Rawat Inap", callback_data="bb4")
button5 = InlineKeyboardButton(text="e.	Informasi Nomor VA", callback_data="bb5")
keyboard_inline3 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)

#Keyboard Inline MutasiData
button1 = InlineKeyboardButton(text="a.	Pendaftaran Peserta Baru", callback_data="cc1")
button2 = InlineKeyboardButton(text="b.	Pengalihan Jenis Kepesertaan", callback_data="cc2")
button3 = InlineKeyboardButton(text="c.	Penonaktifan PPU BU", callback_data="cc3")
button4 = InlineKeyboardButton(text="d.	Aktivasi Anak> 21 Tahun", callback_data="cc4")
keyboard_inline4 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4)

#Keyboard Inline PerubahanData
button1 = InlineKeyboardButton(text="a.	Perubahan Identitas BU", callback_data="dd1")
button2 = InlineKeyboardButton(text="b.	Perubahan PIC BU", callback_data="dd2")
button3 = InlineKeyboardButton(text="c.	Perubahan Identitas Pekerja", callback_data="dd3")
button4 = InlineKeyboardButton(text="d.	Perubahan Faskes", callback_data="dd4")
button5 = InlineKeyboardButton(text="e.	Sinkronisasi Kelas Rawat (Suami Istri Pekerja)", callback_data="dd5")
keyboard_inline5 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)

#Keyboard Inline PenonaktifanVABU
button1 = InlineKeyboardButton(text="a.	Syarat Penutupan VA BU", callback_data="ee1")
keyboard_inline6 = InlineKeyboardMarkup().add(button1)

#Keyboard Inline Edabu
button1 = InlineKeyboardButton(text="a.	Pembuatan Username Edabu", callback_data="ff1")
button2 = InlineKeyboardButton(text="b.	Aktivasi Username Edabu", callback_data="ff2")
button3 = InlineKeyboardButton(text="c.	Ketentuan Login Edabu", callback_data="ff3")
button4 = InlineKeyboardButton(text="d.	Reset Password Edabu", callback_data="ff4")
button5 = InlineKeyboardButton(text="e.	Sosialisasi Edabu (Link Zoom)", callback_data="ff5")
keyboard_inline7 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)

#Keyboard Inline InfoJKN
button1 = InlineKeyboardButton(text="a.	Apa itu JKN?", callback_data="gg1")
button2 = InlineKeyboardButton(text="b.	Regulasi JKN", callback_data="gg2")
button3 = InlineKeyboardButton(text="c.	Segmen Kepesertaan", callback_data="gg3")
button4 = InlineKeyboardButton(text="d.	Besaran Iuran", callback_data="gg4")
button5 = InlineKeyboardButton(text="e.	Manfaat", callback_data="gg5")
button6 = InlineKeyboardButton(text="f.	Alur Pelayanan", callback_data="gg6")
button7 = InlineKeyboardButton(text="g.	Kelas Rawat Inap", callback_data="gg7")
button8 = InlineKeyboardButton(text="h.	Suami Istri Sama-Sama Pekerja", callback_data="gg8")
button9 = InlineKeyboardButton(text="i.	Kanal Pendaftaran", callback_data="gg9")
button10 = InlineKeyboardButton(text="j. Kanal Pengaduan dan Informasi", callback_data="gg10")
button11 = InlineKeyboardButton(text="k. Grup Telegram BU", callback_data="gg11")
button12 = InlineKeyboardButton(text="l. Nomor RO", callback_data="gg12")
button13 = InlineKeyboardButton(text="m. Daftar Faskes Seluruh Indonesia", callback_data="gg13")
keyboard_inline8 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(button7).add(button8).add(button9).add(button10).add(button11).add(button12).add(button13)

#Query Keyboard A
@dp.callback_query_handler(text=["aa1", "aa2", "aa3"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "aa1":
        await call.message.answer(str(
"""
1. Formulir registrasi badan usaha
2. Surat kuasa penggunaan Aplikasi Edabu
3. Format data karyawan (37 Kolom)
4. Surat ijin usaha (NIB/SIUP/TDP/MOU/Akta Yayasan/SKTU) (BU)
5. NPWP (Badan/Perorangan) (BU)
6. KTP dan KK Seluruh Karyawan yang Didaftakan (BU)

(BU)= Disiapkan oleh BU

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "aa2":
        await call.message.answer(str(
"""
1. Surat Permohonan Sertifikat (terlampir)
2. Surat Pernyataan Sertifikat Badan Usaha (terlampir)
3. Bukti bayar iuran bulan terakhir

dokumen yang sudah dilengkapi dapat diserahkan langsung ke Kantor BPJS Kesehatan Cabang Denpasar di Jl. D.I. Panjaitan No.6, Niti Mandala Renon atau dapat dikirimkan via email ke kc-denpasar@bpjs-kesehatan.go.id

Sebagai informasi awal bahwa Sertifikat Kepesertaan BPJS Kesehatan akan diterbitkan bagi Badan Usaha yang telah selesai proses pemeriksaan Kepatuhan oleh Petugas Pemeriksa BPJS Kesehatan. 

Terkait pelaksanaan Pemeriksaan kepatuhan tersebut di atas mohon Bapak/Ibu dapat mempersiapkan data-data pendukung sebagai berikut :
1. Legalitas Pemberi Kerja (SIUP, TDP, NPWP Perusahaan, Akta Pendirian Perusahaan)
2. Data seluruh pekerja meliputi Jenis Kelamin (L/P), Nomor Identitas (KTP & Nomor Kartu BPJS Kesehatan), Status Karyawan (Tetap/Kontrak) (2 bulan terakhir softcopy excel)
3. Data gaji pekerja termasuk komponen upah tetap dan tidak tetap (2 bulan terakhir soft copy excel)
4. Bukti setor gaji pekerja (payrol bank) beserta rinciannya
5. Slip gaji pekerja dan kontrak kerja (sampling)
6. Peraturan Perusahaan/Perjanjian Kerja Bersama
7. Data Wajib Lapor Ketenagakerjaan
8. SPT Pajak Pasal 21 dan Pasal 26 bulan terakhir
9. Absensi pekerja

Data-data tersebut dapat dipersiapkan terlebih dahulu sampai dengan petugas melakukan konfirmasi terkait jadwal pemeriksaan kepatuhan.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "aa3":
        await call.message.answer(str(
"""
1. Surat Permohonan Surat Keterangan Badan Usaha (terlampir)
2. Surat Pernyataan Surat Keterangan Badan Usaha (terlampir)
3. Format data karyawan (terlampir)        
4. Slip Gaji Tanda Terima Karyawan/ Payroll Gaji Karyawan
5. Bukti bayar iuran bulan terakhir

Dokumen yang sudah dilengkapi dapat diserahkan langsung ke Kantor BPJS Kesehatan Cabang Denpasar di Jl. D.I. Panjaitan No.6, Niti Mandala Renon atau dapat dikirimkan via email ke kc-denpasar@bpjs-kesehatan.go.id.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 ' 
"""
        ))

    await call.answer()

#Inline bb1
button1 = InlineKeyboardButton(text="PPU BU", callback_data="bb1.1")
button2 = InlineKeyboardButton(text="PBPU/ Mandiri", callback_data="bb1.2")
keyboard_bb1 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["bb1.1", "bb1.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "bb1.1":
        await call.message.answer(str(
"""
Untuk mengetahui tagihan iuran peserta PPU BU dapat dilakukan melalui aplikasi e-Dabu dengan memilih menu:
1. Menu Laporan
2. Tagihan
3. Pilih bulan tagihan
4. Downlload Billing Statement (password: kode BU contoh: 02330000)
5. Downlload Rincian Tagihan (password: dibuatkan secara mandiri dengan ketentuan minimal 8 digit yang terdiri dari huruf besar, huruf kecil, angka, dan karakter, contoh: Bu12345*)
"""
        ))
    if call.data == "bb1.2":
        await call.message.answer(str(
"""
Untuk mengetahui tagihan iuran peserta PBPU/BP (Mandiri) dapat dilakukan melalui aplikasi Mobile JKN dengan memilih menu:
1. Info Iuran
2. Masukkan No. KIS/No. VA peserta
3. Klik Cari
"""
        ))

    await call.answer()

#Inline bb1
button1 = InlineKeyboardButton(text="PPU BU", callback_data="bb2.1")
button2 = InlineKeyboardButton(text="PBPU/ Mandiri", callback_data="bb2.2")
keyboard_bb2 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["bb2.1", "bb2.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "bb2.1":
        await call.message.answer(str(
"""
Untuk mengetahui tunggakan iuran peserta PPU BU dapat dilakukan melalui aplikasi e-Dabu dengan memilih menu:
1. Menu Laporan
2. Tagihan
3. Pilih bulan tagihan
4. Downlload Billing Statement (password: kode BU contoh: 02330000)
5. Downlload Rincian Tagihan (password: dibuatkan secara mandiri dengan ketentuan minimal 8 digit yang terdiri dari huruf besar, huruf kecil, angka, dan karakter, contoh: Bu12345*)

Informasi tunggakan PPU BU dapat juga diketahui melalui aplikasi M-Banking atau e-Commerce menggunakan kode Virtual Account (VA) Badan Usaha.
Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
        await call.message.answer(str(
"""
[Cara melakukan cicilan tunggakan iuran Badan Usaha yang sempat tutup]
Mohon mengirimkan laporan keuangan dan mutasi rekening selama 3 bulan terakhir dan KTP penanggung jawab (PIC) baru dapat mengirimkan surat permohonan aktivasi badan usaha dan dapat mengirimkan ke email kc-Denpasar@bpjs-kesehatan.go.id dengan batas maksimal mencicil selama 12 kali
"""
        ))
    if call.data == "bb2.2":
        await call.message.answer(str(
"""
Untuk mengetahui tunggakan iuran peserta PBPU/BP (Mandiri) dapat dilakukan melalui aplikasi Mobile JKN dengan memilih menu:
1. Info Iuran
2. Masukkan No. KIS/No. VA peserta
3. Klik Cari
Informasi tunggakan peserta dapat dicek melalui aplikasi M-Banking atau e-Commerce menggunakan kode Virtual Account (VA) peserta.
"""
        ))

    await call.answer()

#Query Keyboard B
@dp.callback_query_handler(text=["bb1", "bb2", "bb3", "bb4", "bb5"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "bb1":
        await call.message.answer(str(
"""
Informasi Terkait Iuran
"""
        ), reply_markup=keyboard_bb1)
    if call.data == "bb2":
        await call.message.answer(str(
"""
Informasi Tunggakan
"""
        ), reply_markup=keyboard_bb2)
    if call.data == "bb3":
        await call.message.answer(str(
"""
Rekonsiliasi peserta dan iuran di BPJS Kesehatan dilakukan memlalui beberapa tahapan sebagai berikut :
1. Adanya peloporan dari peserta/badan usaha
2. Verifikasi oleh petugas
3. Tindaklanjut peloporan
4. Penandatangan Berita Acara Rekonsiliasi

Dalam rangka penandatanganan Berita Acara Rekonsiliasi mohon dapat menyiapkan data berikut:
Nama Lengkap PIC :
Jabatan PIC :
No. HP PIC :
e-Mail BU :

Mohon siapkan nomor surat Berita Acara Rekonsiliasi dan stempel Badan Usaha, serta tentukan jadwal TTD Berita Acara Rekonsiliasi di Kantor BPJS Kesehatan Cabang Denpasar.
"""
        ))
    if call.data == "bb4":
        await call.message.answer(str(
"""
Apabila peserta PPU BU atau PBPU (Mandiri) menunggak iuran dan setelah peserta melunasi tunggakan tersebut maka dalam waktu 45 hari sejak status kepesertaannya aktif kembali, peserta wajib membayar denda pelayanan kesehatan kepada BPJS Kesehatan untuk setiap pelayanan kesehatan rawat inap tingkat lanjutan yang diperolehnya. Denda yang dimaksud yaitu sebesar 5% x estimasi biaya rawat inap x lama bulan tertunggak atau 5% dari perkiraan  biaya paket Indonesian Case Based Groups berdasarkan diagnosa dan prosedur awal untuk setiap bulan tertunggak dengan ketentuan :
a. Jumlah bulan tertunggak paling banyak 12 bulan;
b. Besaran denda paling tinggi adalah Rp 30.000.000,00; dan
c. Jumlah denda akan diinformasikan oleh RS atau faskes tempat peserta akan rawat inap.

Denda pelayanan kesehatan bagi peserta PPU BU dibayarkan oleh Pemberi Kerja.
"""
        ))
    if call.data == "bb5":
        await call.message.answer(str(
"""
Cara menggetahui Virtual Account Badan Usaha:

Pembayaran iuran BPJS Kesehatan dapat dilakukan melalui bank yang bekerjasama dengan BPJS Kesehatan menggunakan kode VA (Virtual Account) Badan Usaha/Peserta Mandiri, tergantung dari jenis kepesertaannya. Berikut adalah rincian kode VA pembayaran iuran BPJS Kesehatan :

*Badan Usaha 
BRI/BNI/BTN/BCA 88888900 + Kode BU (8 digit) 
Bank Mandiri 89888900 + Kode BU (8 digit) 

*Peserta PBPU/BP (Mandiri)
BRI/BNI/BTN/BCA 888880 + 10 digit terakhir nomor KIS
Bank Mandiri 898880 + 10 digit terakhir nomor KIS
"""
        ))

    await call.answer()

#Inline cc
button1 = InlineKeyboardButton(text="Tata Cara Pendaftaran Peserta Baru", callback_data="cc1.1")
button2 = InlineKeyboardButton(text="Tata Cara Pendaftaran Anggota Keluarga (Belum JKN)", callback_data="cc1.2")
button3 = InlineKeyboardButton(text="Tata Cara Pendaftaran Keluarga (Sudah JKN)", callback_data="cc1.3")
button4 = InlineKeyboardButton(text="Tata Cara Pendaftaran Bayi Baru Lahir", callback_data="cc1.4")
button5 = InlineKeyboardButton(text="Tata Cara Pendaftaran Anggota Keluarga Tambahan (1%)", callback_data="cc1.5")
keyboard_cc1 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5)

@dp.callback_query_handler(text=["cc1.1", "cc1.2", "cc1.3", "cc1.4", "cc1.5"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "cc1.1":
        await call.message.answer(str(
"""
Pendaftaran pekerja dan anggota keluarga baru (belum pernah terdaftar JKN
KIS) dapat dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan
agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir), berikut tata
cara pendaftaran melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK 
4. Pilih jenis mutasi "Tambahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pribadi, alamat, faskes, informasi lain)
6. Klik simpan

Jika data gagal diproses melalui e-Dabu, Bapak/Ibu PIC BU dapat mengirimkan
e-Mail ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh)
agar pekerja dan anggota keluarganya dapat terdaftar di bulan berikutnya dengan
melampirkan :
- Capture bukti gagal e-Dabu
- Excel 37 kolom (format terlampir)
- KK Pekerja

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc1.2":
        await call.message.answer(str(
"""
Pendaftaran anggota keluarga baru (belum pernah terdaftar JKN-KIS) dapat dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir), berikut tata cara pendaftaran melalui e-Dabu: 
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Tambah Anggota Keluarga" lalu tekan tombol panah biru
5. Input, dan review form digital (data pribadi, alamat, dan faskes)
6. Klik simpan
"""
        ))
    if call.data == "cc1.3":
        await call.message.answer(str(
"""
Pendaftaran angggota keluarga yang sudah pernah terdaftar JKN-KIS dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya. 
Dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 kolom di sheet "Penambahan Keluarga" (format terlampir)
- Melampirkan scan KK
- Melampirkan surat pernyataan pengunduran diri dari PBI bagi Anggota
keluarga yang sebelumnya terdaftar sebagai PBI (APBN/APBD)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc1.4":
        await call.message.answer(str(
"""
Pendaftaran Bayi Baru Lahir (BBL) dilakukan setelah bayi lahir paling lambat
28 hari sejak kelahirannya melalui beberapa kanal pendaftaran sebagai berikut:
1. Fasilitas Kesehatan (Rumah Sakit bayi dilahirkan)
2. Pandawa di Nomor WA 08118165165
3. Email migrasi di alamat bpjskesehatan.migrasi@gmail.com
Berkas yang perlu dilampirkan antara lain:
- Surat Keterangan Lahir dari fasilitas ksehatan (RS/FKTP)
- KK dan KTP orang tua

Jika usia bayi sudah lebih dari 28 hari, maka orang tua bayi wajib memperbaharui KK terlebih dahulu dan memastikan NIK bayi sudah online di Dukcapil Pusat. Setelah itu PIC Badan Usaha (BU) dapat melakukan input data penambahan anggota keluarga melalui website e-Dabu.
Jika bayi sudah terdaftar a/n Bayi Nyonya, maka tidak perlu didaftarkan kembali. Peserta hanya perlu mengupdate identitas melalui e-Mail migrasi (bpjskesehatan.migrasi@gmail.com) dengan melampirkan Form 37 Kolom dan scan KK yang sudah diperbaharui.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc1.5":
        await call.message.answer(str(
"""
Pendaftaran angggota keluarga tambahan (orang tua, mertua, anak ke-4, dst) dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya, dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 kolom di sheet "Penambahan Keluarga" (format terlampir)
- Melampirkan scan KK
- Melampirkan surat kuasa pemotongan gaji 1% (format terlampir)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))

    await call.answer()

#Inline cc
button1 = InlineKeyboardButton(text="Dari PBI JK (APBN) ke PPU BU", callback_data="cc2.1")
button2 = InlineKeyboardButton(text="Dari PBPU/BP Pemda (APBN) ke PPU BU", callback_data="cc2.2")
button3 = InlineKeyboardButton(text="Dari PBPU (Mandiri) ke PPU BU", callback_data="cc2.3")
button4 = InlineKeyboardButton(text="Dari PPU BU ke PPU BU", callback_data="cc2.4")
button5 = InlineKeyboardButton(text="Dari PPU PPNPN ke PPU BU", callback_data="cc2.5")
button6 = InlineKeyboardButton(text="Pengalihan Tanggungan (Istri, Suami dan Anak) Menjadi Pekerja di PPU BU", callback_data="cc2.6")
keyboard_cc2 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6)

@dp.callback_query_handler(text=["cc2.1", "cc2.2", "cc2.3","cc2.4", "cc2.5", "cc2.6"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "cc2.1":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari segmen PBI JK (PBI APBN) ke segmen PPU BU dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir). 
Berikut tata cara pengaliham jenis kepesertaan dari segmen PBI JK (PBI APBN) ke segmen PPU BU melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Pindahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pekerjaan , data keluarga)
6. Klik simpan
Jika data gagal diproses melalui aplikasi e-Dabu, mohon mengirimkan email ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh) dengan berkas yang dilampirkan sebagai berikut:
- Capture bukti gagal di e-Dabu
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK
- Melampirkan surat pernyataan pengunduran diri dari PBI  (format terlampir)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc2.2":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari segmen PBPU Pemda (PBI APBD) ke segmen PPU BU dilakukan melalui dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya, dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK
- Melampirkan surat pernyataan pengunduran diri dari PBI  (format terlampir)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc2.3":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari segmen PBPU (Mandiri) ke segmen PPU BU dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir). 
Berikut tata cara pengaliham jenis kepesertaan dari segmen PBPU (Mandiri) ke segmen PPU BU melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Pindahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pekerjaan , data keluarga)
6. Klik simpan
Jika data gagal diproses melalui aplikasi e-Dabu, mohon mengirimkan email ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh) dengan berkas yang dilampirkan sebagai berikut:
- Capture bukti gagal di e-Dabu
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc2.4":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari segmen PPU BU ke segmen PPU BU dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir). 
Berikut tata cara pengaliham jenis kepesertaan dari segmen PPU BU ke segmen PPU BU melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Pindahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pekerjaan , data keluarga)
6. Klik simpan
Jika data gagal diproses melalui aplikasi e-Dabu, mohon mengirimkan email ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh) dengan berkas  yang dilampirkan sebagai berikut:
- Capture bukti gagal di e-Dabu
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc2.5":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari segmen PPU PPNPN ke segmen PPU BU dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir). 
Berikut tata cara pengaliham jenis kepesertaan dari segmen PPU PPNPN ke segmen PPU BU melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Pindahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pekerjaan , data keluarga)
6. Klik simpan
Jika data gagal diproses melalui aplikasi e-Dabu, mohon mengirimkan email ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh) dengan berkas  yang dilampirkan  sebagai berikut:
- Capture bukti gagal di e-Dabu
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc2.6":
        await call.message.answer(str(
"""
Pengalihan jenis kepesertaan dari dari tanggungan PPU (suami/istri/anak) menjadi Pekerja PPU BU dilakukan melalui aplikasi e-Dabu sampai dengan H-1 akhir bulan agar terdaftar di bulan berikutnya (User manual e-Dabu terlampir). 
Berikut tata cara pengaliham jenis kepesertaan dari tanggungan PPU (suami/istri/anak) menjadi Pekerja PPU BU melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Pindahkan Sebagai Pekerja" lalu tekan tombol panah biru
5. Input, dan review form digital (data pekerjaan , data keluarga)
6. Klik simpan
Jika data gagal diproses melalui aplikasi e-Dabu, mohon mengirimkan email ke bpjskesehatan.migrasi@gmail.com maksimal di tanggal 20 (dua puluh) dengan berkas yang dilampirkan sebagai berikut:
- Capture bukti gagal di e-Dabu
- Mengisi form 37 kolom di sheet "Mutasi ke BU" (format terlampir)
- Melampirkan scan KK

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))

    await call.answer()

#Inline cc
button1 = InlineKeyboardButton(text="Penonaktifan Pekerja", callback_data="cc3.1")
button2 = InlineKeyboardButton(text="Penonaktifan Anggota Keluarga", callback_data="cc3.2")
button3 = InlineKeyboardButton(text="Penonaktifan Sementara (Keluar Negeri)", callback_data="cc3.3")
button4 = InlineKeyboardButton(text="Syarat Penonaktifan PPU BU", callback_data="cc3.4")
keyboard_cc3 = InlineKeyboardMarkup().add(button1).add(button2).add(button3).add(button4)

@dp.callback_query_handler(text=["cc3.1", "cc3.2", "cc3.3","cc3.4"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "cc3.1":
        await call.message.answer(str(
"""
[Tanpa Jaminan Kesehatan]

Penonaktifan pekerja tanpa jaminan kesehatan selama 6 bulan adalah penonaktifan dengan kriteria sebegai berikut :
1. Pekerja resign/mengundurkan diri;
2. Habis masa kontrak;
3. Pensiun;
4. Mangkir; atau
5. Meninggal.

Penonaktifan pekerja dilakukan melalui aplikasi e-Dabu paling lambat tanggal 20 agar nonkatif per tanggal 1 bulan berikutnya. Berikut tata cara penonaktifannya melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Non Aktif selain  PHK" lalu tekan tombol panah biru
5. Input, dan review form digital (data penonaktifan (masukan no HP dan email pekerja, masukan nomor surat dari BU), data PHK, Daftar Dokumen, Syarat dan Ketentuan)
6. Klik simpan

Selanjutnya. Badan Usaha mengirimkan dokumen penonaktifan ke email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat 2 hari setelah  penonaktifan di e-Dabu. Berikut link untuk mengunduh dokumen penonaktifan.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
        await call.message.answer(str(
"""
[Dengan Jaminan Kesehatan]

Penonaktifan pekerja dengan jaminan kesehatan selama 6 bulan adalah penonaktifan dengan kriteria PHK sebegai berikut :
1. PHK yang sudah ada Putusan Hubungan Industrial, dibuktikan dengan putusan/akta pengadilan hubungan industrial;
2. PHK karena penggabungan perusahaan, dibuktikan dengan akta notaris;
3. PHK karena perusahaan pailit atau mengalami kerugian, dibuktikan dengan keputusan kepailitan dari pengadilan; atau
4. PHK karena pekerja mengalami sakit yang berkepanjangan dan tidak mampu bekerja, dibuktikan dengan surat dokter.

Penonaktifan pekerja dilakukan melalui aplikasi e-Dabu paling lambat tanggal 20 agar nonkatif per tanggal 1 bulan berikutnya. Berikut tata cara penonaktifannya melalui e-Dabu:
1. Pilih menu peserta  
2. Pilih input data
3. Input NIK/ No. KIS Pekerja 
4. Pilih jenis mutasi "Non Aktif PHK" lalu tekan tombol panah biru
5. Input, dan review form digital (data penonaktifan (masukan no HP dan email pekerja, masukan nomor surat dari BU), data PHK, Daftar Dokumen, Syarat dan Ketentuan)
6. Klik simpan

Selanjutnya. Badan Usaha mengirimkan dokumen penonaktifan ke email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat 2 hari setelah  penonaktifan di e-Dabu. Berikut link untuk mengunduh dokumen penonaktifan.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc3.2":
        await call.message.answer(str(
"""
Penonaktifan anggota keluarga dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya, dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 Kolom sheet "Nonaktif"
- Melampirkan KK Peserta
- Surat Pernyataan Penonaktifan Anggota Keluarga dari Badan Usaha (format terlampir).
Selanjutnya, anggota keluarga yang telah dinonaktifkan dari tanggungan PPU BU wajib dialihkan menjadi peserta Program JKN sesuai dengan jenis kepesertaan yang seharusnya. Khusus untuk pengalihan menjadi peserta Mandiri dapat dilakukan melalui Pandawa (Pelayanan Administrasi Melalui WA) di 08118165165 atau datang langsung ke kantor cabang BPJS Kesehatan terdekat dengan membawa persyaratan pendaftaran peserta Mandiri.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "cc3.3":
        await call.message.answer(str(
"""
Bagi peserta Program JKN yang akan tinggal di luar negeri lebih dari 6 bulan dapat melaporkan penonaktifan kepesertaan Program JKN-KIS pada bulan keberangkatan ke luar negeri melalui Kantor BPJS Kesehatan terdekat atau melalui Pelayanan Administrasi melalui WA (Pandawa) di 08118165165 dengan melengkapi dokumen berupa Kartu Keluarga, Passport, dan salah satu dokumen berikut:
1. Visa Peserta dan/atau Anggota Keluarga;
2. Izin Tinggal di Luar Negeri;
3. Surat Tugas Belajar;
4. Surat Tugas Bekerja;
5. Surat Pernyataan Penghentian Pembayaran Gaji Dari Pemberi Kerja; atau
6. Surat Pemberitahuan dari Sponsor.
Pastikan sebelum melakukan pelaporan ke BPJS Kesehatan, peserta yang bersangkutan telah melunasi iuran BPJS Kesehatan s/d bulan keberangkatan ke luar negeri.

Peserta yang kembali ke Indonesia wajib mengaktifkan kembali kepesertaan Program JKN-KIS melalui Kantor BPJS Kesehatan terdekat atau melalui Pandawa dengan melengkapi dokumen berupa:
1. Passport;
2. Kartu Keluarga;
3. Buku Rekening Bank Mandiri/BRI/BNI/BCA; dan
4. Materai 10.000 (2 lembar).

Jika peserta yang bersangkutan kembali ke Indonesia sebelum 6 bulan, maka tagihan akan terhitung sejak bulan pertama setelah iuran terakhir dibayarkan. Jika peserta kembali ke Indonesia setelah lebih dari 6 bulan, maka tagihan akan dihitung sejak yang bersangkutan kembali ke Indonesia.
"""
        ))
    if call.data == "cc3.4":
        await call.message.answer(str(
"""
Terlampir kami kirimkan link untuk mengunduh dokumen penonaktifan untuk dapat digunakan selanjutnya. Dokumen yang dilengkapi disesuaikan dengan jenis/keterangan penonaktifan sebagai berikut:
1. Resign : Form 1, 2, 3, dan Surat Resign
2. Meninggal : Form 1, 2, 3, dan Akta Kematian/Surat Keterangan Meninggal
3. Habis Kontrak : Form 1, 2, 3, dan 4
4. Penisun : Form 1, 2, 3, dan 5
5. Mangkir : Form 1, 2, 3, dan 5
6. Pemecatan Sepakat : Form 1, 2, 3, dan 5

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))

    await call.answer()

#Query C
@dp.callback_query_handler(text=["cc1", "cc2", "cc3", "cc4"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "cc1":
        await call.message.answer(str(
"""
a. Pendaftaran Peserta Baru
"""
        ), reply_markup=keyboard_cc1)
    if call.data == "cc2":
        await call.message.answer(str(
"""
b. Pengalihan Jenis Kepesertaan
"""
        ), reply_markup=keyboard_cc2)
    if call.data == "cc3":
        await call.message.answer(str(
"""
c. Penonaktifan PPU BU
"""
        ), reply_markup=keyboard_cc3)
    if call.data == "cc4":
        await call.message.answer(str(
"""
Aktivasi anak dari PPU  BU yang berusia lebih dari 21 Tahun dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya, dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 Kolom di sheet "Penambahan Keluarga"
- Melampirkan scan Surat Keternagan Aktif Kuliah
- Melampirkan scan KK

Jika tidak dilakukan pelaporan aktivasi, maka kepesertaan anak tersebut dinonaktifkan secara otomatis oleh sistem yang mengakbiatkan yang bersangkutan tidak dapat mendapatkan jaminan pelayanan kesehatan.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))

    await call.answer()

#Query D
@dp.callback_query_handler(text=["dd1", "dd2", "dd3", "dd4", "dd5"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "dd1":
        await call.message.answer(str(
"""
Perubahan identitas Badan Usaha dapat dilakukan dengan cara mengirimkan e-Mail ke kc-denpasar@bpjs-kesehatan.go.id dengan melampirkan :
- Surat Permohonan Perubahan Identitas BU
- Mengisi form registrasi dengan identitas yang terbaru (centang di bagian perubahan identitas)
- Akta Perubahan Nama BU (jika BU mengalami perubahan nama)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "dd2":
        await call.message.answer(str(
"""
Perubahan PIC Badan Usaha dapat dilakukan dengan cara mengirimkan e-Mail ke kc-denpasar@bpjs-kesehatan.go.id dengan melampirkan :
- Surat Permohonan Perubahan PIC BU
- Mengisi form registrasi dengan identitas yang terbaru (centang di bagian perubahan id entitas)
- Surat Kuasa Penggunaan e-Dabu (jika BU mengalami perubahan nama PIC)

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "dd3":
        await call.message.answer(str(
"""
Perubahan identitas pekerja (Nama, NIK, Nomor KK, Alamat, Nomor HP, Email) dilakukan melalui email migrasi di alamat bpjskesehatan.migrasi@gmail.com paling lambat tanggal 20 setiap bulannya, dengan mengirimkan berkas sebagai berikut: 
- Mengisi form 37 Kolom sheet "Identitas"
- Melampirkan scan KK

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    if call.data == "dd4":
        await call.message.answer(str(
"""
Perubahan Fasiltas Kesehatan Tingkat Pertama//Faskes Tk. 1 dilakukan maksimal 1 (satu) kali dalam 3 (tiga) bulan melalui aplikasi Mobile JKN pada menu "Ubah Data Peserta".

Perubahan Faskes Tk. 1 yang dialkukan dalam bulan berjalan akan aktif di Faskes Tk. 1 yang baru pada tanggal 1 bulan berikutnya.
"""
        ))
    if call.data == "dd5":
        await call.message.answer(str(
"""
Permohonan sinkronisasi hak kelas peserta suami dan istri yang sama-sama menjadi pekerja dilakukan dengan cara mengirim form 37 Kolom (sheet IDENTITAS) dan melampirkan scan KK peserta ke email migrasi di alamat bpjskesehatan.migrasi@gmail.com dengan subjek "Sinkronisasi Hak Kelas Peserta Suami dan Istri".

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))

    await call.answer()

#Query E
@dp.callback_query_handler(text=["ee1"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "ee1":
        await call.message.answer(str(
"""
Alur/mekanisme terkait penutupan kepesertaan Badan Usaha (Penutupan Virtual Account) pada Program JKN di BPJS Kesehatan adalah sebagai berikut :
1. Badan Usaha melakukan penonaktifan karyawan melalui Aplikasi e-Dabu dan melengkapi dokumen penonaktifan melalui email migrasi (bpjskesehatan.migrasi@gmail.com).
2. Badan Usaha menyerahkan dokumen permohonan penonaktifan Virtual Account Badan Usaha berupa :
   - Surat permohonan penutupan Virtual Account Badan Usaha yang ditandatangani oleh pimpinan, bermaterai 10.000, dan distempel
   - Surat keterangan penutupan Badan Usaha dari Dinas Tenaga Kerja/Perijinan atau Akta pembubaran/penutupan Badan Usaha dari Notaris/pejabat berwenang
   - Bukti pembayaran iuran terakhir bulan pengajuan penutupan

Dokumen penutupan VA dapat dikirimkan melalui email BPJS Kesehatan Cabang Denpasar di kc-denpasar@bpjs-kesehatan.go.id atau dapat diserahkan secara langsung ke kantor BPJS Kesehatan Cabang Denpasar yang beralamat di Jl. Panjaitan No.6, Niti Mandala, Renon.

Anda dapat mengakses link berikut :
' https://bit.ly/lampiranbubpjs2022 '
"""
        ))
    await call.answer()

#Query F
@dp.callback_query_handler(text=["ff1", "ff2", "ff3", "ff4", "ff5"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "ff1":
        await call.message.answer(str(
"""
Dalam rangka pembuatan.username aplikasi e-Dabu badan usaha, mohon dapat melengkapi data sebagai berikut :
- Nama BU : 
- Kode BU : 
- Alamat email : 
- Nama lengkap PIC :
- NIK PIC :
- Tgl lahir PIC :
- No HP PIC :

Selanjutnya, data yang sudah dilengkapi dikirimkan ke RO sesuai dengan wilayah kerja masing-masing RO (link terlampir) atau dikirimkan ke Grup Badan Usaha KC Denpasar
( https://bit.ly/Grup_BU_KC_Dps_Nov22 )
"""
        ))
    if call.data == "ff2":
        await call.message.answer(str(
"""
Dalam rangka aktivasi.username aplikasi e-Dabu badan usaha, mohon dapat melengkapi data sebagai berikut :
- Nama BU : 
- Username BU : 
- Alamat email BU : 

Selanjutnya, data yang sudah dilengkapi dikirimkan ke RO sesuai dengan wilayah kerja masing-masing RO (link terlampir) atau dikirimkan ke Grup Badan Usaha KC Denpasar
( https://bit.ly/Grup_BU_KC_Dps_Nov22)

Untuk menghindari adanya penonaktifan username di kemudian hari, dimohon agar badan usaha melakukan login ke e-Dabu minimal 1 (satu) kali dalam 1 (satu) bulan.
"""
        ))
    if call.data == "ff3":
        await call.message.answer(str(
"""
Berikut adalah beberapa hal yang perlu diperhatikan pada saat login e-Dabu Badan Usaha :
1. Pastikan Badan Usaha telah memiliki user e-Dabu BU
2. Gunakan PC/Komputer/Laptop, bukan smartphone
3. Pastikan koneksi internet stabil
4. Bersihkan cache and cookies pada browser
5. Link e-Dabu telah sesuai : https://edabu.bpjs-kesehatan.go.id/Edabu/Home/Login
6. Pastikan user e-Dabu aktif. Jika user nonaktif dikarenakan tidak ada aktifitas selama 90 hari, mohon dapat diinfokan melalui grup Badan Usaha dengan format "Mohon aktivasi user e-Dabu PT/CV/UD .................."
7. Pastikan Username dan password sesuai. Jika lupa password bisa reset password di e-Dabu pada menu awal saat login dengan cara klik "LUPA PASSWORD"
"""
        ))
    if call.data == "ff4":
        await call.message.answer(str(
"""
Reset password aplikasi edabu dilakukan dengan memilih fitur/hyperlink LUPA PASSWORD? KLIK DISINI yang ada di link https://edabu.bpjs-kesehatan.go.id/Edabu/home/Login.

Mohon unntuk menyiapkan data username dan email badan usaha. Setelah menginput username dan email badan usaha, link perubahan password akan dikirim ke email di tersebut, selanjutnya Bapak/Ibu dapat membuatkan password baru dengan ketentuan minimal 8 digit terdiri dari huruf besar, huruf kecil, angka dan karakter. 
"""
        ))
    if call.data == "ff5":
        await call.message.answer(str(
"""
Bersama ini kami sampaikan bahwa  Sosialisasi e-Dabu dilaksanakan setiap hari Selasa dan Kamis Pukul 10.00 WITA. Bagi Bapak/Ibu PIC yang berkenan mengikuti kegiatan sosialisasi tersebut bisa bergabung melalui link zoom meeting berikut : 
https://bit.ly/Sos_e-Dabu 
Meeting ID : 81811945950
Passcode  : BPJSKes
"""
        ))

    await call.answer()

#Keyboard GG3~5,G7,G12
#Inline GG
button1 = InlineKeyboardButton(text="PBI", callback_data="gg3.1")
button2 = InlineKeyboardButton(text="Non-PBI", callback_data="gg3.2")
keyboard_gg3 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["gg3.1", "gg3.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg3.1":
        await call.message.answer(str(
"""
Peserta Penerima Bantuan Iuran Jaminan Kesehatan (PBI JK) adalah Peserta yang tergolong fakir miskin dan orang tidak mampu yang iurannya dibayarkan oleh Pemerintah,

Peserta PBI JK ditetapkan oleh Menteri yang menyelenggarakan urusan Pemerintahan di bidang sosial. Bayi yang dilahirkan oleh ibu kandung yang terdaftar sebagai peserta PBI JK secara otomatis ditetapkan  sebagai peserta PBI JK sesuai dengan ketentuan peraturan perundang-undangan.
"""
        ))
    if call.data == "gg3.2":
        await call.message.answer(str(
"""
[PPU BU]

Pekerja Penerima Upah (PPU) Badan Usaha adalah setiap orang yang bekerja pada Pemberi Kerja dengan menerima Gaji atau Upah pada suatu Badan Usaha.
Pekerja Penerima Upah Selain Penyelenggara Negara (PPU BU) terdiri atas:
a)      Pegawai Badan Usaha Milik Negara (BUMN) adalah pegawai pada badan usaha yang seluruh atau sebagian besar modalnya dimiliki oleh negara melalui penyertaan secara langsung yang berasal dari kekayaan negara yang dipisahkan.
b)     Pegawai Badan Usaha Milik Daerah (BUMD) adalah  pegawai pada badan usaha yang didirikan dan dimiliki oleh Pemerintah Daerah.
c)      Pegawai Badan Usaha Swasta (BU Swasta) adalah pegawai pada badan usaha yang dimiliki oleh swasta. Badan Usaha ini sepenuhnya dikelola dan permodalannya dari pihak swasta dan berbadan hukum. Beberapa jenis BU Swasta yang ada di Indonesia seperti Perusahaan Perorangan, Perusahaan Persekutuan, Perusahaan Perseroan, Yayasan, dan lain-lain
"""
        ))
        await call.message.answer(str(
"""
[PBPU]

Pekerja Bukan Penerima Upah (PBPU) adalah setiap orang yang bekerja atau berusaha atas risiko sendiri, misalnya petani, nelayan, mekanik, dll
"""
        ))
        await call.message.answer(str(
"""
[BP]

Bukan Pekerja (BP) terdiri atas:
1)     Investor yaitu perorangan yang melakukan suatu investasi (bentuk penanaman modal sesuai dengan jenis investasi yang dipilihnya) baik dalam jangka pendek atau jangka panjang.
2)     Pemberi Kerja
3)     Penerima Pensiun, terdiri atas:
4)     Veteran
5)     Perintis Kemerdekaan 
6)     Bukan Pekerja yang tidak termasuk angka 1 sampai dengan angka 6 yang mampu membayar iuran
"""
        ))

    await call.answer()

#Inline GG
button1 = InlineKeyboardButton(text="PBI", callback_data="gg4.1")
button2 = InlineKeyboardButton(text="Non-PBI", callback_data="gg4.2")
keyboard_gg4 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["gg4.1", "gg4.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg4.1":
        await call.message.answer(str(
"""
Iuran PBI JK sebesar Rp. 42.000/orang/bulan yang dibayarkan oleh Pemerintah.
"""
        ))
    if call.data == "gg4.2":
        await call.message.answer(str(
"""
[PPU BU]

Iuran bagi Peserta Pekerja Penerima Upah yang bekerja di BUMN, BUMD dan Swasta sebesar 5% ( lima persen) dari Gaji atau Upah per bulan dengan ketentuan : 4% (empat persen) dibayar oleh Pemberi Kerja dan 1% (satu persen) dibayar oleh Peserta. Iuran untuk keluarga tambahan Pekerja Penerima Upah yang terdiri dari anak ke 4 dan seterusnya, ayah, ibu dan mertua, besaran iuran sebesar sebesar 1% (satu persen) dari dari gaji atau upah per orang per bulan, dibayar oleh pekerja penerima upah.
"""
        ))
        await call.message.answer(str(
"""
[PBPU]

a.	Sebesar Rp. 42.000, - (empat puluh dua ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas III.
Khusus untuk kelas III, bulan Juli - Desember 2020, peserta membayar iuran sebesar Rp. 25.500, -. Sisanya sebesar Rp 16.500,- akan dibayar oleh pemerintah sebagai bantuan iuran.
Per 1 Januari 2021, iuran peserta kelas III yaitu sebesar Rp 35.000,-, sementara pemerintah tetap memberikan bantuan iuran sebesar Rp 7.000,-.
b.	Sebesar Rp. 100.000,- (seratus ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas II.
c.	Sebesar Rp. 150.000,- (seratus lima puluh ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas I.
"""
        ))
        await call.message.answer(str(
"""
[BP]

a.	Sebesar Rp. 42.000, - (empat puluh dua ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas III.
Khusus untuk kelas III, bulan Juli - Desember 2020, peserta membayar iuran sebesar Rp. 25.500, -. Sisanya sebesar Rp 16.500,- akan dibayar oleh pemerintah sebagai bantuan iuran.
Per 1 Januari 2021, iuran peserta kelas III yaitu sebesar Rp 35.000,-, sementara pemerintah tetap memberikan bantuan iuran sebesar Rp 7.000,-.
b.	Sebesar Rp. 100.000,- (seratus ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas II.
c.	Sebesar Rp. 150.000,- (seratus lima puluh ribu rupiah) per orang per bulan dengan manfaat pelayanan di ruang perawatan Kelas I.
"""
        ))

    await call.answer()

#Inline GG
button1 = InlineKeyboardButton(text="Dijamin", callback_data="gg5.1")
button2 = InlineKeyboardButton(text="Tidak Dijamin", callback_data="gg5.2")
keyboard_gg5 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["gg5.1", "gg5.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg5.1":
        await call.message.answer(str(
"""
Pelayanan kesehatan yang dijamin terdiri atas: 
a. Pelayanan kesehatan tingkat pertama, meliputi pelayanan kesehatan nonspesialistik

b. Pelayanan kesehatan tingkat rujukan, meliputi: administrasi pelayanan; pemeriksaan, pengobatan, dan konsultasi medis dasar; pemeriksaan, pengobatan, dan konsultasi medis spesialistik; tindakan medis spesialistik baik bedah maupun nonbedah sesuai dengan indikasi medis; pelayanan obat, alat kesehatan, dan bahan medis habis pakai; pelayanan penunjang diagnostik lanjutan sesuai dengan indikasi medis
"""
        ))
    if call.data == "gg5.2":
        await call.message.answer(str(
"""
Pelayanan kesehatan yang tidak dijamin meliputi:
a. pelayanan kesehatan yang tidak sesuai dengan ketentuan perundang-undangan;

b. pelayanan kesehatan yang tidak bekerja sama dengan BPJS Kesehatan kecuali dalam keadaan darurat;

c. Pelayanan kesehatan terhadap penyakit atau cedera akibat kecelakaan kerja atau hubungan kerja yang telah dijamin oleh program jaminan kecelakaan kerja atau menjadi tanggungan pemberi kerja;

d. pelayanan kesehatan yang dijamin oleh program jaminan kecelakaan lalu lintas yang bersifat wajib sampai nilai yang ditanggung program jaminan kecelakaan lalu lintas sesuai hak kelas rawat peserta;

e. pelayanan kesehatan yang dilakukan di luar negeri;

f. pelayanan kesehatan untuk tujuan estetik;

g. pelayanan kesehatan untuk mengatasi infertilitas;

h. pelayanan meratakan gigi/ ortodonsi;

i. gangguan kesehatan/ penyakit akibat ketergantungan obat dan/ atau alkohol;

j. gangguan kesehatan akibat sengaja menyakiti diri sendiri atau akibat melakukan hobi yang membahayakan diri sendiri;

k. pengobatan komplemmenter, alternatif, dan tradisional yang belum dinyatakan efektif berdasarkan penilaian teknologi kesehatan

l. pengobatan dan tindakan medis yang dikategorikan sebagai percobaan atau eksperimen;

m. alat dan obat kontrasepsi, kosmetik;

n. perbekalan kesehatan rumah tangga;

o. pelayanan kesehatan akibat bencana pada masa tanggap darurat, kejadian luar biasa/ wabah;

p. pelayanan kesehatan pada kejadian tak diharapkan yang dapat dicegah;

q. pelayanan kesehatan yang diselenggarakan dalam rangka bakti sosial;

r. pelayanan kesehatan akibat tindak pidana penganiayaan, kekerasan seksual, korban terorisme, dan tindak pidana perdagangan prang sesuai dengan ketentuan peraturan perundang-undangan;

s. pelayanan kesehatan tertentu yang berkaitan dengan Kementrian Pertahanan, TNI, dan Polri;

t. pelayanan lainnya yang tidak ada hubungan dengan manfaat jaminan kesehatan yang diberikan; 

u. pelayanan yang sudah ditanggung dalam program lain;

v. rujukan atas permintaan sendiri;

w. gangguan kesehatan akibat sengaja menyakiti diri sendiri, melakukan hobi yang membahayakan diri sendiri, dan kejadian yang dapat dicegah/ dihindari.
"""
        ))

    await call.answer()

#Inline GG
button1 = InlineKeyboardButton(text="PBI", callback_data="gg7.1")
button2 = InlineKeyboardButton(text="Non-PBI", callback_data="gg7.2")
keyboard_gg7 = InlineKeyboardMarkup().add(button1).add(button2)

@dp.callback_query_handler(text=["gg7.1", "gg7.2"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg7.1":
        await call.message.answer(str(
"""
Peserta PBI JK yang iurannya dibayarkan oleh Pemerintah mendapat manfaat pelayanan kesehatan di ruang perawatan kelas III
"""
        ))
    if call.data == "gg7.2":
        await call.message.answer(str(
"""
[PPU BU]

a. PPU BU yang memperoleh gaji sampai dengan Rp. 4.000.000 mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas II.
b. PPU BU yang memperoleh gaji lebih  dari Rp. 4.000.000 mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas I.
"""
        ))
        await call.message.answer(str(
"""
[PBPU]

a. Peserta yang membayar iuran sebesar Rp. 42.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas III.
b. Peserta yang membayar iuran sebesar Rp. 100.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas II.
c. Peserta yang membayar iuran sebesar Rp. 150.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas I.
"""
        ))
        await call.message.answer(str(
"""
[BP]

a. Peserta yang membayar iuran sebesar Rp. 42.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas III.
b. Peserta yang membayar iuran sebesar Rp. 100.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas II.
c. Peserta yang membayar iuran sebesar Rp. 150.000, mendapat manfaat pelayanan kesehatan di ruang perawatan Kelas I.
"""
        ))

    await call.answer()

#Inline GG
button1 = InlineKeyboardButton(text="Denpasar", callback_data="gg12.1")
button2 = InlineKeyboardButton(text="Badung", callback_data="gg12.2")
button3 = InlineKeyboardButton(text="Tabanan", callback_data="gg12.3")
keyboard_gg12 = InlineKeyboardMarkup().add(button1).add(button2).add(button3)

@dp.callback_query_handler(text=["gg12.1", "gg12.2", "gg12.3"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg12.1":
        await call.message.answer(str(
"""
[DENPASAR]

Koordinator RO Denpasar Utara, Denpasar Timur, Denpasar Selatan
Moh.Waris Sabar - wa.me/+628113110405
https://t.me/MWSabar 

RO
1. Denpasar Selatan (Sanur, Sanur Kaja, Sanur Kauh, Renon Panjer, Sidakarya) 
2. Denpasar Timur (Seluruh Desa/Kelurahan Kec. Denpasar Timur)
I Putu Agus Prasatya Putra - wa.me/+628113866464
https://t.me/agusprastya 

RO
1. Denpasar Selatan (Sesetan, Pemogan, Pedungan, Serangan)
2. Denpasar Utara (Seluruh Desa/Kelurahan Kec. Denpasar Utara)
Werenvrida Priliani Haki - wa.me/+628113951408
https://t.me/Priliani 
Koordinator RO Wilayah Denpasar Barat
Gaspar Yuniar Wadja - wa.me/+628113860675
https://t.me/Opagaspar 

RO
1. Denpasar Barat (Seluruh Desa/Kelurahan Kec. Denpasar Barat
I Putu Yoga Kusuma Widnyana - wa.me/+628113862608
https://t.me/yoga_kusuma
"""
        ))
    if call.data == "gg12.2":
        await call.message.answer(str(
"""
[BADUNG]

Koordinator RO Wilayah Badung
Ni Wayan Ratna Pertiwi - wa.me/+628113893288 
https://t.me/Nanapertiwinew 

RO
1. Kuta Selatan ( Seluruh Desa/Kelurahan Kec. Kuta Selatan)
Bima Arief Pratama - wa.me/+62852340844285
https://t.me/tuanbima 

RO
1. Kuta ( Seluruh Desa/Kelurahan Kec. Kuta)
I.G.A. Feby Purnami Dewi - wa.me/+628113311505
https://t.me/+628113311505 

RO
1. Mengwi (Seluruh Desa/Kelurahan Kec.Mengwi)
2. Abiansemal (Seluruh Desa/Kelurahan Kec Abiansemal)
3. Petang (Seluruh Desa/Kelurahan Kec. Kuta Utara)
I Made Tony Anggara - wa.me/+6281139617030
https://t.me/tony_anggara 

RO
1. Kuta Utara (Seluruh Desa/ Kelurahan Kec. Kuta Utara)
Kadek Wiryawan - wa.me/+628113802207
https://t.me/Wiryaartha
"""
        ))
    
    if call.data == "gg12.3":
        await call.message.answer(str(
"""
[TABANAN]

Koordinator RO Wilayah Tabanan
Desak Gede Novi Mahayanti - wa.me/+628119992181
https://t.me/Novidesak 

RO 
1. Seluruh Tabanan (Seluruh Desa/Kelurahan Kab. Tabanan)
Ni Luh Putu Nita Marini - wa.me/+628113279900
https://t.me/+628113279900
"""
        ))

    await call.answer()

#Query G
@dp.callback_query_handler(text=["gg1", "gg2", "gg3", "gg4", "gg5", "gg6", "gg7", "gg8", "gg9", "gg10", "gg11", "gg12", "gg13"])
async def inline1(call: types.CallbackQuery):
    
    if call.data == "gg1":
        await call.message.answer(str(
"""
Hallo Peserta dari JKN-KIS, semoga dalam keadaan sehat selalu.  Seringkali masyarakat belum dapat membedakan antara JKN, BPJS Kesehatan dan KIS  sehingga menganggap ketiga hal ini merupakan hal yang sama, padahal itu berbeda lho, berikut merupakan penjelasan dari JKN, BPJS Kesehatan dan KIS:

1.  Jaminan Kesehatan adalah jaminan berupa perlindungan kesehatan agar Peserta memperoleh manfaat pemeliharaan kesehatan dan perlindungan dalam memenuhi kebutuhan dasar kesehatan yang diberikan kepada setiap orang yang telah membayar Iuran Jaminan Kesehatan atau Iuran Jaminan Kesehatannya dibayar oleh Pemerintah Pusat atau Pemerintah Daerah.

2.  Badan Penyelenggara Jaminan Sosial Kesehatan yang selanutnya disingkat BPJS Kesehatan adalah badan hukum yang dibentuk untuk menyelenggarakan program Jaminan Kesehatan

3.  KIS (Kartu Indonesia Sehat): merupakan identitas fisik peserta Jaminan Kesehatan Nasional. Saat ini Kartu Indonesia Sehat sudah tersedia secara online melalui aplikasi Mobile JKN yang dapat di unduh melalui Playstore (android), dan App Store (IOS)
"""
        ))
    if call.data == "gg2":
        await call.message.answer(str(
"""
Berikut ini merupakan beberapa landasan Hukum utama yang mengatur BPJS Kesehatan, dan program JKN:
1.  Undang-Undang Dasar 1945
2.  Undang-Undang Nomor 40 Tahun 2004 tentang Sistem Jaminan Sosial Nasional 
3.  Undang-Undang Nomor 24 Tahun 2011 tentang Badan Penyelenggara Jaminan Sosial
4.  Peraturan Presiden Nomor 82 Tahun 2018
5.  Peraturan Presiden Nomor 64 Tahun 2020
6.  Instruksi Presiden Republik Indonesia Nomor 1 Tahun 2022
"""
        ))
    if call.data == "gg3":
        await call.message.answer(str(
"""
Silahkan pilih Segmen Kepesertaan untuk:
"""
        ), reply_markup=keyboard_gg3)
    if call.data == "gg4":
        await call.message.answer(str(
"""
Silahkan pilih Besaran Iuran untuk:
"""
        ), reply_markup=keyboard_gg4)
    if call.data == "gg5":
        await call.message.answer(str(
"""
Silahkan pilih:
"""
        ), reply_markup=keyboard_gg5)
    if call.data == "gg6":
        await call.message.answer(str(
"""
1.	Pasien bukan gawat darurat (Non Emergency)

Peserta yang membutuhkan pelayanan kesehatan namun bukan dalam keadaan gawat darurat wajib berkunjung terlebih dahulu ke Fasilitas Kesehatan Tingkat Pertama (Puskesmas/Klinik/Dokter Perorangan) sesuai dengan faskes terdaftarnya. Jika membautuhkan pelayanan yang bersifat spesialistik atau sub spesialistik maka peserta dirujuk secara berjenjang ke Rumah Sakit untuk mendapatkan pelayanan kesehatan lebih lanjut.

2. Pasien gawat darurat (Emergency)

Peserta dengan kondisi gawat darurat yaitu peserta yang membutuhkan pelayanan medis segera, karena jika tidak ditolong maka kondisi pasien akan lebih parah dan dapat mengancam keselamatan peserta. Untuk kondisi gawat darurat pesreta dapat langsung mengakses pelayanan kesehatan ke fasilitas kesehatan terdekat baik itu RS atau FKTP yang bekerjasam maupun yang tidak bekerja sama dengan BPJS Kesehatan.
"""
        ))
    if call.data == "gg7":
        await call.message.answer(str(
"""
Silahkan pilih Kelas Rawat Inap berdasarkan:
"""
        ), reply_markup=keyboard_gg7)
    if call.data == "gg8":
        await call.message.answer(str(
"""
Dalam hal pasangan suami istri yang masing-masing merupakan pekerja maka keduancya wajib didaftarkan sebagai peserta PPU oleh masing-masing pemberi kerja dan membayar iuran. Suami, istri dan anak dari peserta PPU berhak memilih kelas perawatan tertinggi.
"""
        ))
    if call.data == "gg9":
        await call.message.answer(str(
"""
Berikut kami sampaikan kanal pendaftaran peserta sebagai berikut :
-	Aplikasi Mobile JKN
-	Melalui Panduan layanan WA Pandawa di Nomor wa.me/+628118165165
-	Mengontak RO sesuai dengan wilayah (untuk badan usaha)
"""
        ))
    if call.data == "gg10":
        await call.message.answer(str(
"""
Berikut kami sampaikan kanal permintaan informasi dan pengaduan peserta sebagai berikut :
1.  Aplikasi Mobile JKN dapat anda downloada pada Playstore, dan Appstore
2.  BPJS Kesehatan Care Center silahkan hubungi pada nomor 165
3.  CHIKA (Chat Asisstant JKN) pada telegram dengan link https://t.me/Chika_BPJSKesehatan_bot
4.  PANDAWA (Pelayanan Administrasi Melalui Whatsapp) dapat dihubungi lewat nomor WhatsApp wa.me/+628118165165
5.  Website BPJS Kesehatan dapat diakses lewat link  www.bpjs-kesehatan.go.id.
6.  Kantor Cabang dan Kantor Kabupaten/Kota
"""
        ))
    if call.data == "gg11":
        await call.message.answer(str(
"""
Berikut kami sampaikan link grup telegram Badan Usaha KC Denpasar sebagai sarana penyampaian informasi, diskusi dan penyampaian kendala kepesertaan di badan usaha:

https://bit.ly/Grup_BU_KC_Dps_Nov22
"""
        ))
    if call.data == "gg12":
        await call.message.answer(str(
"""
Silahkan memilih sesuai lokasi cabang terdekat dari anda:
"""
        ), reply_markup=keyboard_gg12)
    if call.data == "gg13":
        await call.message.answer(str(
"""
Berikut kami kirimkan link untuk melakukan proses pengecekan FKTP (Fasilitas Kesehatan Tingkat Pertama) di seluruh Indonesia :
https://faskes.bpjs-kesehatan.go.id
"""
        ))

    await call.answer()



executor.start_polling(dp)

import time 
import sys
import os

idenama,idennim,idenjudul,identglpinjam,identglkembali= [], [], [], [], []
class perpustakan:
    def menu (self):
        print(''' 
        ===================================================
        ****sistem pinjam buku perpustakaan digital****
        pilih menu :
        1. pinjam buku
        2. kembalikan buku
        3. cetak struk bukti buku 
        4. cek daftar buku lengkap 
        5. lihat history peminjaman buku
        0. matikan aplikasi 
        ===================================================
        ''')

        while True:
            pil = int(input('\nmasukkan pilihan anda : '))
            if(pil==1):
                pilih.Pinjambuku()
                pilih.ulang()
            elif(pil==2):
                pilih.kembalikanbuku()
                pilih.ulang()
            elif(pil==3):
                pilih.cetakstruk()
                pilih.ulang()
            elif(pil==4):
                pilih.daftarbuku()
                pilih.ulang()
            elif(pil==5):
                pilih.historypinjaman()
                pilih.ulang()
            elif(pil==0):
                time.sleep(0.5)
                print('TERIMAKASIH SAMPAI JUMPA KEMBALI')
                quit ()
            else:
                print('pilihan tidak tersedia')
                pilih.ulang()
    def ulang(self):
        time.sleep(2)
        ulang = input('apakah anda ingin mencoba lagi? [Y/N]')
        print('=============================================\n')
        if (ulang=='yes' or ulang== 'Yes' or ulang== 'Y' or ulang== 'y'):
            pilih.menu()
        elif (ulang=='no' or ulang== 'No' or ulang== 'N' or ulang== 'n'):
            time.sleep(0.5)
            print('Terimakasih, sampai jumpa kembali')
            quit()
        else:
            print('INPUTAN ANDA SALAH ! PILIH (Y) ATAU (N) !' )
            pilih.ulang()
    def pinjambuku(self):
        print('silahkan masukkan data diri anda')
        nama = str(input('Nama peminjam Buku:'))
        while True:
            try:
                nim=int(input("NIM: "))
                break 
            except ValueError:
                print('inputan anda salah ! Silahkan ulangi kembali...!')
        judul= str(input('judul buku:'))
        tglpinjam= str(input('tanggal pinjam buku:'))
        tglkembali= str(input('tanggal pengembalian buku:'))
        while True:
            try:
                banyak = int(input('banyaknya buku yang dipinjam :'))
                break 
            except ValueError:
                print("Inputan Anda Salah ! Silahkan ulangi kembali....")
        konfirm = str(input('Apakah Data diri anda sudah benar? [Y/N]'))
        for i in range(1):
            idenama.append (nama)
            idennim.append (nim) 
            idenjudul.append(judul)
            identglpinjam.append(tglpinjam)
            identglkembali.append(tglkembali)
            if (konfirm == 'Yes' or konfirm== 'yes' or konfirm== 'Y' or konfirm== 'y'):
                print(''''
                Terimakasih telah meminjam buku ditempat kami, kami berharap agar anda dapat 
                mengembalikan buku dengan tepat waktu\n''')
                print('========SILAHKAN AMBIL STRUK ANDA========')
                print('----------------------------------------')
                sys.stdout = open("struk.txt","w")
                print('''
                    ======Sistem Peminjaman Buku Perpustakaan Digital========
                    =================STRUK BUKTI PINJAM=====================
                ''')


time.sleep(2)
pilih=perpustakan()
pilih.menu()

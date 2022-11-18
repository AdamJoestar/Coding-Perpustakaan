#Codingan Perpustakaan
def garis():
    print(30*'=')
garis()
print("SELAMAT DATANG DI PERPUSTAKAAN WIBU")
garis()

def lobby():
    print("Pilih Menu yang Diinginkan ")
    print("1.List Buku\n2.Meminjam Buku")
def pilih():  
    awal=int(input("Masukkan Menu Yang Dipilih : "))
    if awal == 1 :
        print("KODE     Jenis Buku     Harga Jaminan")
        garis()
        print("C    ChainsawMan     Rp.5000")
        print("N    Naruto          Rp.6000")
        print("A    AttackOnTitan   Rp.7000")
        pilih()
    else :           
        garis()
        keranjang1=[]
        keranjang2=[]
        keranjang3=[]
        keranjang4=[]
        bj=int(input("Banyak Jenis Buku Yang Dipinjam"))

        total=0
        for i in range(bj):
            print("Jenis Ke-",i+1)
            kp=input("Kode Buku [C/N/A] : ")
            bp=int(input("Banyak Buku Yang Dipinjam : "))
            keranjang3.append(bp)
            if kp=="C":
                jenis="Chainsawman"
                harga=5000
            elif kp=="N":
                jenis="Naruto"
                harga=6000
            else:
                jenis="AttackOnTitan"
                harga=7000
            keranjang1.append(jenis)
            keranjang2.append(harga)

            jmlharga=harga*bp
            keranjang4.append(jmlharga)
            total=total+jmlharga
            admin=int(total*0.1)
            totalbayar=total+admin

            garis()
            print("Perpustakaan WIBU")
            garis()
            print("NO\t Jenis Buku\t Harga Jaminan Satuan\t Banyak Buku\t Jumlah Harga")
            garis()

            for i in range(bj):
                print(i+1,"\t",keranjang1[i],"\t\t\t",keranjang2[i],"\t\t\t\t",keranjang3[i],"\t\t\t\t",keranjang4[i])
            garis()

            print("\t\t\t\tJaminan  :",total)
            print("\t\t\t\tBiaya Admin  :",admin)
            print("\t\t\t\tTotal Bayar  :",totalbayar)
            garis()
            print("Tunjukkan Bukti Peminjaman Buku Ini Pada SAat Pengembalian Buku Untuk Mengambil Uang Jaminan")
            garis()
            print("Arigatou")

            baliklagi=input("Mau meminjam [YA/TIDAK]?")
            if baliklagi=="YA" or baliklagi=="ya":
                lobby()
            else :
                exit()
lobby()
pilih()

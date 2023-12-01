tahun_lahir = int(input("masukan tahun lahir anda :"))
jenis_kelamin = input("masukan jenis kelamin :")
kelahiran = input("dimana anda tinggal :")
tahun_sekarang = 2023
umur = tahun_sekarang - tahun_lahir
print("umur anda" , umur)


if umur > 18 or kelahiran == "jakarta" or jenis_kelamin == "laki-laki":
    print("anda sudah bisa membuat ktp")
else :
    print("anda masih di bawah umur")
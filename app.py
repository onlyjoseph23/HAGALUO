from flask import Flask, render_template, request

app = Flask(__name__)

# Data produk tiruan ala Ruparupa
DAFTAR_PRODUK = [
    {"id": 1, "nama": "Lemari Pakaian Minimalis 3 Pintu", "harga": "Rp 2.500.000", "kategori": "Furniture", "gambar": "https://via.placeholder.com/300x200?text=Lemari+Pakaian", "deskripsi": "Lemari pakaian modern dengan cermin besar dan ruang penyimpanan luas.", "ukuran": "120 x 50 x 180 cm"},
    {"id": 2, "nama": "Sofa Tamu L-Shape Modern", "harga": "Rp 4.200.000", "kategori": "Living", "gambar": "https://via.placeholder.com/300x200?text=Sofa+Modern", "deskripsi": "Sofa empuk berkualitas tinggi untuk mempercantik ruang keluarga.", "ukuran": "210 x 85 x 90 cm"},
    {"id": 3, "nama": "Meja Makan Kayu Jati 4 Kursi", "harga": "Rp 3.800.000", "kategori": "Dining", "gambar": "https://via.placeholder.com/300x200?text=Meja+Makan", "deskripsi": "Set meja makan minimalis berbahan kayu jati kokoh dan elegan.", "ukuran": "140 x 80 x 75 cm"},
    {"id": 4, "nama": "Rak Buku Dinding Industrial", "harga": "Rp 750.000", "kategori": "Storage", "gambar": "https://via.placeholder.com/300x200?text=Rak+Buku", "deskripsi": "Rak buku gantung bergaya industrial untuk efisiensi ruangan.", "ukuran": "80 x 20 x 60 cm"}
]

@app.route('/')
def beranda():
    keyword = request.args.get('q', '').lower()
    if keyword:
        hasil_pencarian = [p for p in DAFTAR_PRODUK if keyword in p['nama'].lower()]
        return render_template('index.html', produk_list=hasil_pencarian, pencarian=keyword)
    return render_template('index.html', produk_list=DAFTAR_PRODUK, pencarian="")

@app.route('/detail/<int:id_produk>')
def detail_produk(id_produk):
    produk_terpilih = next((p for p in DAFTAR_PRODUK if p["id"] == id_produk), None)
    return render_template('detail.html', produk=produk_terpilih)

if __name__ == '__main__':
    app.run(debug=True)
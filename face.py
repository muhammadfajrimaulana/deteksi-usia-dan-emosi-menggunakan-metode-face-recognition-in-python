import cv2
import numpy as np

# Inisialisasi detektor wajah OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fungsi untuk memprediksi usia (dummy)
def predict_age(face):
    # Biasanya, ini akan menggunakan model pembelajaran mendalam yang dilatih untuk prediksi usia.
    # Sebagai pengganti, kita gunakan nilai dummy.
    return 25

# Fungsi untuk mendeteksi ekspresi wajah
def detect_emotion(face, prev_emotion, frame_count, update_interval):
    # Misalnya, Anda memiliki model yang dilatih sebelumnya untuk mendeteksi emosi
    # Implementasi ini akan berbeda tergantung pada model yang Anda gunakan.
    # Di sini, sebagai contoh, kita menggunakan array label emosi.
    emotions = ["Happy", "Sad", "Angry", "Surprise", "Fear", "Neutral", "Disgust"]
    
    # Update ekspresi wajah setiap setelah melewati sejumlah frame tertentu
    if frame_count % update_interval == 0:
        # Prediksi emosi (misalnya menggunakan model yang telah dilatih sebelumnya)
        # Di sini, kita hanya mengembalikan emosi acak untuk tujuan demonstrasi.
        new_emotion = np.random.choice(emotions)
    else:
        new_emotion = prev_emotion
    
    return new_emotion

# Buka koneksi ke webcam (0 adalah kamera default)
face = cv2.VideoCapture(0)

# Inisialisasi variabel untuk menyimpan ekspresi wajah dari frame sebelumnya
prev_emotion = None

# Inisialisasi variabel untuk menghitung frame
frame_count = 0

# Set interval untuk memperbarui ekspresi wajah (dalam jumlah frame)
update_interval = 10

while True:
    # Tangkap bingkai demi bingkai
    ret, frame = face.read()

    # Periksa apakah bingkai terbaca dengan benar
    if not ret:
        break

    # Konversi frame ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah menggunakan detektor wajah Haar
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        
        # Prediksi usia (dummy)
        age = predict_age(gray[y:y+h, x:x+w])
        
        # Deteksi emosi
        emotion = detect_emotion(gray[y:y+h, x:x+w], prev_emotion, frame_count, update_interval)
        
        # Simpan ekspresi wajah untuk penggunaan pada frame berikutnya
        prev_emotion = emotion
        
        # Gambar persegi panjang di sekitar wajah
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Tampilkan usia di atas persegi panjang wajah
        cv2.putText(frame, f'Age: {age}', (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        
        # Tampilkan emosi di bawah persegi panjang wajah
        cv2.putText(frame, f'Emotion: {emotion}', (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Tampilkan bingkai yang dihasilkan
    cv2.imshow('frame', frame)

    # Update frame count
    frame_count += 1

    # Putuskan loop dengan menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Lepaskan tangkapan dan tutup semua jendela OpenCV
face.release()
cv2.destroyAllWindows()

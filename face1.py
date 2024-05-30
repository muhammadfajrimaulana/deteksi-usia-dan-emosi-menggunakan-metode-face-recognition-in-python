# import cv2

# # Buka koneksi ke webcam (0 adalah kamera default)
# face = cv2.VideoCapture(0)

# while True:
#     # Tangkap bingkai demi bingkai
#     ret, frame = face.read()

#     # Periksa apakah bingkai terbaca dengan benar
#     if not ret:
#         break

#     # Tampilkan bingkai yang dihasilkan
#     cv2.imshow('frame', frame)

#     # Putuskan loop dengan menekan tombol 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# #  Lepaskan tangkapan dan tutup semua jendela OpenCV
# face.release()
# cv2.destroyAllWindows()


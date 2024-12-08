import cv2

# Thử đọc file ảnh
image = cv2.imread('eaut.jpg')
if image is None:
    print("Không thể đọc file ảnh.")
else:
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

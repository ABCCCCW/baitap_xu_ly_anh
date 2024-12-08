import cv2
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import pytesseract
import time
#Thêm đường dẫn file tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from openpyxl import  load_workbook #kết nối với file excel
#Thiết lập camera
cap = cv2.VideoCapture(1)
#Tạo giao diện bằng tkinter
root = Tk()
root.geometry('1300x770')
root.resizable(width=False, height=False) #cố định khung
root.title("TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN")
root.configure(bg='white')
#Giao diện chữ
tentruong = Label(root, text="TRƯỜNG ĐẠI HỌC CÔNG NGHỆ ĐÔNG Á ", bg='white',font=('Time 25 bold'))
tentruong.pack(side=TOP)
a = Label(root, text="      ", bg='white',font=('Time 5 bold'))
a.pack(side=TOP)
khoa = Label(root, text="KHOA CÔNG NGHỆ THÔNG TIN", bg='white',font=('Time 22 bold'))
khoa.pack(side=TOP)
b = Label(root, text="      ", bg='white',font=('Time 5 bold'))
b.pack(side=TOP)
hocphan = Label(root, text="HỌC PHẦN XỬ LÝ ẢNH VÀ THỊ GIÁC MÁY TÍNH", bg='white',font=('Time 20 bold'))
hocphan.pack(side=TOP)
c = Label(root, text="    ", bg='white',font=('Time 30 bold'))
c.pack(side=TOP)
doan = Label(root, text="BÀI TẬP LỚN", bg='white', fg='red',font=('Time 30 bold'))
doan.pack(side=TOP)
detai = Label(root, text="TRÍCH XUẤT THÔNG TIN TỪ THẺ SINH VIÊN", bg='white', fg='red', font=('Time 30 bold'))
detai.pack(side=TOP)
kiemtra = Label(root, text="Nếu thông tin chính xác hãy nhấn NHẬP DỮ LIỆU", bg='white', fg='blue', font=('Time 20 bold'))
kiemtra.place(x= 630, y= 643)
thoigian = Label(root, text="Vui lòng kiểm tra thông tin", bg='white', fg='blue', font=('Time 25 bold'))
thoigian.place(x= 740, y= 350)
#Giao diện khung chữ
gd_hoten = Label(root, text="Họ và tên:", bg='white', fg='black', font=('Time 18 bold'))
gd_hoten.place(x= 745, y= 425)
gd_ngaysinh = Label(root, text="Ngày sinh:", bg='white', fg='black', font=('Time 18 bold'))
gd_ngaysinh.place(x= 745, y= 460)
gd_msv = Label(root, text="Mã Sinh Viên:", bg='white', fg='black', font=('Time 18 bold'))
gd_msv.place(x= 745, y= 495)
gd_khoa = Label(root, text="Khóa:", bg='white', fg='black', font=('Time 18 bold'))
gd_khoa.place(x= 745, y= 530)
gd_gtthe = Label(root, text="Giá Trị Thẻ:", bg='white', fg='black', font=('Time 18 bold'))
gd_gtthe.place(x= 745, y= 565)
#Chèn logo vào giao diện
logo = cv2.imread('eaut.jpg')
logo = cv2.resize(logo, (200, 200))
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
img = Image.fromarray(logo)
img = ImageTk.PhotoImage(image=img)
imglabel = Label(root, image=img)
imglabel.place(x=0, y=0)
logo1 = cv2.imread('khoacntt.jpg')
logo1 = cv2.resize(logo1, (195, 195))
logo1 = cv2.cvtColor(logo1, cv2.COLOR_BGR2RGB)
img1 = Image.fromarray(logo1)
img1 = ImageTk.PhotoImage(image=img1)
img1label = Label(root, image=img1)
img1label.place(x=1095, y=0)
#Số thứ tự bắt đầu từ 0
i = 0
#Set frame lên giao diện
canvas = Canvas(root, width= 480, height= 320, bg= "black")
canvas.place(x= 100, y= 350)
#Frame
def display():
#Khai báo biến toàn cục
    global canvas, image
#Resize khung hình
    _, frame = cap.read()
    frame = cv2.resize(frame, (480, 320))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.create_image(0, 0, image=image, anchor=NW)
#Sau 1 ms thì update khung hình
    root.after(1, display)
display()
#Trích xuất thông tin
def txtt():
    global imgcharTEN, imgcharNS, imgcharMSV, imgcharKHOA, imgcharGTRITHE, time_string

    # Đọc ảnh từ camera
    _, frame = cap.read()
    
    # Cắt từng khung ảnh chứa dữ liệu y,x
    TEN = frame[215:243, 305:520]
    NS = frame[240:265, 305:439]
    MSV = frame[265:290, 305:439]
    KHOA = frame[290:315, 305:439]
    GTRITHE = frame[310:340, 405:536]
    
    
    # Chuyển ảnh xám
    cutTEN = cv2.cvtColor(TEN, cv2.COLOR_BGR2GRAY)
    cutNS = cv2.cvtColor(NS, cv2.COLOR_BGR2GRAY)
    cutMSV = cv2.cvtColor(MSV, cv2.COLOR_BGR2GRAY)
    cutKHOA = cv2.cvtColor(KHOA, cv2.COLOR_BGR2GRAY)
    cutGTRITHE = cv2.cvtColor(GTRITHE, cv2.COLOR_BGR2GRAY)
    
    # Hiển thị các hình ảnh xám để kiểm tra
    cv2.imshow('cutTEN', cutTEN)
    cv2.imshow('cutNS', cutNS)
    cv2.imshow('cutMSV', cutMSV)
    cv2.imshow('cutKHOA', cutKHOA)
    cv2.imshow('cutGTRITHE', cutGTRITHE)

    # Phân ngưỡng
    ret, threshTEN = cv2.threshold(cutTEN, 110, 255, cv2.THRESH_BINARY_INV)
    ret, threshNS = cv2.threshold(cutNS, 80, 255, cv2.THRESH_BINARY_INV)
    ret, threshMSV = cv2.threshold(cutMSV, 70, 255, cv2.THRESH_BINARY_INV)
    ret, threshKHOA = cv2.threshold(cutKHOA, 75, 255, cv2.THRESH_BINARY_INV)
    ret, threshGTRITHE = cv2.threshold(cutGTRITHE, 78, 240, cv2.THRESH_BINARY_INV)
    
    # Hiển thị các khung ảnh đã phân ngưỡng để kiểm tra
    cv2.imshow('threshTEN', threshTEN)
    cv2.imshow('threshNS', threshNS)
    cv2.imshow('threshMSV', threshMSV)
    cv2.imshow('threshKHOA', threshKHOA)
    cv2.imshow('threshGTRITHE', threshGTRITHE)

    # Chuyển hình ảnh sang chuỗi
    imgcharTEN = pytesseract.image_to_string(threshTEN, lang='vie')
    imgcharNS = pytesseract.image_to_string(threshNS)
    imgcharMSV = pytesseract.image_to_string(threshMSV)
    imgcharKHOA = pytesseract.image_to_string(threshKHOA)
    imgcharGTRITHE = pytesseract.image_to_string(threshGTRITHE)
    
   # Giao diện chữ đã nhận dạng
    hoten_gd = Label(root, text=imgcharTEN, width=20, height=2, bg='white', font=('Time 18 bold'))
    hoten_gd.place(x=915, y=425)
    ngaysinh_gd = Label(root, text=imgcharNS, width=10, height=2, bg='white', font=('Time 18 bold'))
    ngaysinh_gd.place(x=955, y=460)
    msv_gd = Label(root, text=imgcharMSV, width=10, height=2, bg='white', font=('Time 18 bold'), justify='left')
    msv_gd.place(x=955, y=495)
    khoa_gd = Label(root, text=imgcharKHOA, width=10, height=2, bg='white', font=('Time 18 bold'))
    khoa_gd.place(x=955, y=530)
    gtrithe_gd = Label(root, text=imgcharGTRITHE, width=20, height=2, bg='white', font=('Time 18 bold'))
    gtrithe_gd.place(x=875, y=565)
    
    
    # In chữ xuống terminal
    print("Họ và tên:", imgcharTEN)
    print("Ngày sinh:", imgcharNS)
    print("Mã Sinh Viên:", imgcharMSV)
    print("Khóa:", imgcharKHOA)
    print("Hạn Thẻ:", imgcharGTRITHE)

# Nhập dữ liệu qua excel
def get_data():
    global i, wb, ws
    named_tuple = time.localtime()
    time_string = time.strftime("%H:%M:%S-%d/%m/%Y", named_tuple)
    wb = load_workbook('ListSV.xlsx')
    ws = wb.active
    ws.append([i + 1, imgcharTEN.strip(), imgcharNS.strip(), imgcharMSV.strip(), imgcharKHOA.strip(), imgcharGTRITHE.strip(), time_string])
    wb.save('ListSV.xlsx')
    i = i + 1
# Messagebox
    messagebox.showinfo('Thông báo', 'Bạn đã nhập dữ liệu thành công')
# Nút nhấn trích xuất dữ liệu
btn_txtt = Button(root, text='Trích xuất thông tin', bg='green', fg='white', font=('Time 15 bold'))
btn_txtt.config(command=txtt)
btn_txtt.place(x=220, y=700)
# Nút nhấn nhập dữ liệu
btn_get = Button(root, text='Nhập dữ liệu', bg='green', fg='white', font=('Time 15 bold'))
btn_get.config(command=get_data)
btn_get.place(x=880, y=700)
# Kết thúc chương trình
root.mainloop()

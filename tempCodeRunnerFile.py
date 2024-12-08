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
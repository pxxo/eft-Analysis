import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    h, w, _ = frame.shape[:3]  # 追加部分

    w_center = w // 2  # 追加部分
    h_center = h // 2  # 追加部分

    cv2.rectangle(
        frame,
        (w_center - 71, h_center - 71),  # 追加部分
        (w_center + 71, h_center + 71),
        (255, 0, 0),
    )  # 追加部分
    cv2.imshow("frame", frame)  # 追加部分

    k = cv2.waitKey(1) & 0xFF
    prop_val = cv2.getWindowProperty("frame", cv2.WND_PROP_ASPECT_RATIO)

    if k == ord("q") or (prop_val < 0):
        break
    elif k == ord("s"):
        im = frame[h_center - 70 : h_center + 70, w_center - 70 : w_center + 70]  # 追加部分
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 追加部分

        _, th = cv2.threshold(im, 0, 255, cv2.THRESH_OTSU)  # 追加部分
        th = cv2.bitwise_not(th)  # 追加部分
        th = cv2.GaussianBlur(th, (9, 9), 0)  # 追加部分
        cv2.imwrite("capture.jpg", th)
        break

cap.release()
cv2.destroyAllWindows()

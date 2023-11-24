import numpy as np
import cv2 as cv

click_flag = 1


def oncall_mouse(event, x, y, flags, param):
    global click_flag
    if event == cv.EVENT_FLAG_LBUTTON:
        click_flag = not click_flag


cap1 = cv.VideoCapture('../video/vtest.avi')
cap2 = cv.VideoCapture('../video/video1.mp4')

fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter('../video/lab2_output.avi', fourcc, 20, (768, 576))

cv.namedWindow('test:')

while cap1.isOpened():
    flag1, frame1 = cap1.read()
    flag2, frame2 = cap2.read()
    roi = frame2[300:300 + 576, 300:300 + 768]
    # print("Shape of frame1:", frame1.shape)
    # print("Shape of roi:", roi.shape)

    if flag1 and flag2:
        frame_output = cv.addWeighted(frame1, 0.2, roi, 0.8, 0)

        text = 'Hello, World!'
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        color = (0, 0, 255)
        thickness = 2
        linetype = cv.LINE_AA

        (text_width, text_height), _ = cv.getTextSize(text, font, font_scale, thickness)

        x_center = (frame_output.shape[1] - text_width) // 2
        y_center = (frame_output.shape[0] + text_height) // 2
        org = (x_center, y_center)

        cv.setMouseCallback('test:', oncall_mouse)
        if click_flag == 1:
            cv.putText(frame_output, text, org, font, font_scale, color, thickness, linetype)

        output.write(frame_output)

        cv.imshow('test:', frame_output)
        k = cv.waitKey(1)
        if ord('q') == k:
            break

cap1.release()
cap2.release()
output.release()
cv.destroyAllWindows()

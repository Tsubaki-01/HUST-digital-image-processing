import cv2
import numpy as np

# initialize the list of rectangles and boolean indicating
# whether cropping is being performed or not
rectangles = []
current_rectangle = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global rectangles, current_rectangle, cropping

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        rectangles.append([x, y])

        cv2.imshow("image", image)
        cv2.circle(image, (x, y), 0, (0, 255, 0), 10)

        cv2.imshow("image", image)


# load the image, clone it, and setup the mouse callback function
image = cv2.imread('../img/1.jpg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# reset selection when 'r' is pressed
# confirm selection when 'c' is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()
    elif key == ord("c"):
        break

# apply perspective transformation if user made a valid selection
if len(rectangles) == 4:
    pts = np.array(rectangles, dtype=np.int32)
    cv2.polylines(image, [pts], True, (0, 255, 0), 8)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    # map rectangle to square
    src = np.float32(rectangles)
    dst = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(clone, M, (clone.shape[1], clone.shape[0]))
    cv2.imshow("warped", warped)
    cv2.waitKey(0)

# close all open windows
cv2.destroyAllWindows()

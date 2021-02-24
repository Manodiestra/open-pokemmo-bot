from captureScreen import capture_screen
import cv2 as cv
import numpy as np
import captureScreen

def find_pokemon(needle):

    #haystack_img = cv.imread('poke_img/pokemmo_horda_shelmet.png', cv.IMREAD_UNCHANGED)
    print("Needle:", needle)

    if needle == "shelmet":
        needle_img = cv.imread('poke_img/pokemmo_single_shelmet.png', cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2RGB)
    elif needle == "success":
        needle_img = cv.imread('poke_img/success_sweet_scent.png', cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2RGB)
    elif needle == "noPP":
        needle_img = cv.imread('poke_img/no_pp_sweet_scent.png', cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2RGB)

    haystack_img = captureScreen.capture_screen()
    #haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2RGB)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]


    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print('Best match top left position: %s' % str(max_loc))
    print('Best match confidence: %s' % max_val)

    threshold = 0.5
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles.append(rect)

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)

    if locations:
        return 1
    else:
        return 0

    '''
    if len(rectangles):
        return 1

        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        # Loop over all the locations and draw their rectangle
        for (x, y, w, h) in rectangles:
            # Determine the box positions
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            # Draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

        cv.imshow('Matches', haystack_img)
        cv.waitKey()

    else:
        return 0
'''

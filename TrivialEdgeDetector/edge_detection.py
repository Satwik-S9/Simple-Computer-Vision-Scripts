import cv2 as cv
import numpy as np


def pad_image(image, how, value):
    rows, cols = image.shape[0], image.shape[1]
    padded_img = []

    # for 3 channel color images
    if len(image.shape) == 3:
        if how == 'both':
            padder1 = np.zeros((rows, value, 3))
            padded_img = np.hstack((image, padder1))
            
            rows, cols = padded_img.shape[0], padded_img.shape[1]
            padder2 = np.zeros((value, cols, 3))
            padded_img = np.vstack((padded_img, padder2))

        elif how == 'bottom':
            padder = np.zeros((value, cols, 3))
            padded_img = np.vstack((image, padder))

        elif how == 'left':
            padder = np.zeros((rows, value, 3))
            padded_img = np.hstack((image, padder))

    # for grayscale and black & white images
    else:
        if how == 'both':
            padder1 = np.zeros((rows, value))
            padded_img = np.hstack((image, padder1))
            
            rows, cols = padded_img.shape[0], padded_img.shape[1]
            padder2 = np.zeros((value, cols))
            padded_img = np.vstack((padded_img, padder2))

        elif how == 'bottom':
            padder = np.zeros((value, cols))
            padded_img = np.vstack((image, padder))

        elif how == 'left':
            padder = np.zeros((rows, value))
            padded_img = np.hstack((image, padder))
    
    return padded_img

def shift_image(img, pixels: tuple):
    num_rows, num_cols = img.shape[0], img.shape[1]
    translation_matrix = np.float32([[1., 0., pixels[0]], [0., 1., pixels[1]]])
    shifted_img = cv.warpAffine(img, translation_matrix, (num_cols+pixels[0], num_rows+pixels[1])) 
    
    return shifted_img

def detect_edges_trivial(img, display=False):
    shifted_image = shift_image(img, (1, 0))
    padded_img = pad_image(img, 'left', 1)
    
    edges = padded_img - shifted_image
    if display:
        cv.imshow('EDGES', edges)
    
    return edges


if __name__ == '__main__':
    img_path = '/home/freyr/dev/python/opencv/Resources/Photos/cats.jpg'
    img = cv.imread(img_path)
    
    # grayscale image
    gi = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gi', gi)

    #* TESTING AND DEBUGGING
    # pi = pad_image(gi, 'left', 1)
    # si = shift_image(img, (10, 0))
    # cv.imshow("si", si)
    # cv.imshow('pi', pi)
    # print(f"gi: {gi.shape}, pi: {pi.shape}, si: {si.shape}")
    
    edges = detect_edges_trivial(gi, True)
    print(edges.shape)
    edges2 = detect_edges_trivial(img, False)
    cv.imshow('EDGES2', edges2)

    cv.waitKey(0)
    cv.destroyAllWindows()
    
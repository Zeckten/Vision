from pathlib import Path
import time

import numpy as np
import cv2

def init_output_dir(dir):
    output_dir = Path(dir)

    output_dir.mkdir(exist_ok=True)

    for f in output_dir.iterdir():
        if f.is_file():
            f.unlink()

    return output_dir

if __name__ == '__main__':

    output_dir = init_output_dir('calib_imgs')
            
    cap = cv2.VideoCapture(6)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    pattern_width = 8
    pattern_height = 27
    diagonal_dist = 30e-3
    pattern_size = (pattern_width, pattern_height)
    tracker_img = None
    img_ind = 0
    while True:
        ret,frame = cap.read()
        
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            ret, centers = cv2.findCirclesGrid(gray, pattern_size, None, cv2.CALIB_CB_ASYMMETRIC_GRID)
            if ret:
                if tracker_img is None:
                    tracker_img = np.zeros((int(gray.shape[0]/4), int(gray.shape[1]/4)), dtype=np.uint8)
                
                cv2.imwrite(str(output_dir/'frame-{:04d}.png'.format(img_ind)), gray)
                img_ind += 1
                cv2.drawChessboardCorners(frame, pattern_size, centers, ret)
                cv2.imshow('detect',frame)
                for i in range(centers.shape[0]):
                    tracker_img[int(centers[i,0,1]/4), int(centers[i,0,0]/4)]=255

                cv2.imshow('tracker', tracker_img)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

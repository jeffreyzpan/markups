import cv2
import numpy as np

class HighlightExtractor: # TODO: create generic Extractor class & inherit
    """
    Class used to extract highlighted regions from an image
    """
    def __init__(self):
        """
        Initialize highlight extractor with upper and lower HSV bounds to filter out highlight color
        """
        # decent bounds for yellow highlighting
        self.lowerb = np.array([23, 50, 50])
        self.upperb = np.array([40, 255, 255])
        # TODO: create data structure that defines these bounds and allow user to pass in bounds for custom highlight color

    def extract(self, src):
        """
        Extract highlighted regions of a BGR image based on upper and lower HSV bounds

        Args:
            src (np.array): BGR source image
        
        Returns:
            np.array: The masked image
        """
        src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(src_hsv, self.lowerb, self.upperb)

        # Remove isolated regions of mask
        kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (5, 5))
        cv2.erode(mask, kernel, mask)
        cv2.dilate(mask, kernel, mask)

        return mask

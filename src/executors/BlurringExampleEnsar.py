"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.RotationExampleEnsar.src.utils.response import build_response_blurring
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel


class BrightnessExampleEnsar(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")
        print(self.keep_side,"  ",self.rotation_degree)

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def blurring(self, img):
        ksize = (30, 30)
        return  cv2.blur(img, ksize, cv2.BORDER_DEFAULT)

    def flipping(self, img):
        return cv2.flip(img, 1)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.blurring(img.value)
        img.value = self.flipping(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_blurring(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()

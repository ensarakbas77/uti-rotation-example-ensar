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


class BlurringExampleEnsar(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")
        self.secondImage = self.request.get_param("inputSecondImage")
        self.flipParameter = self.request.get_param("FlipParameter")
    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def blurring(self, img, img2):
        ksize = (30, 30)
        task1 = cv2.blur(img, ksize, cv2.BORDER_DEFAULT)
        task2 = cv2.blur(img2, ksize, cv2.BORDER_DEFAULT)
        return  task1, task2

    def flipping(self, img, img2):
        task1 = cv2.flip(img, self.flipParameter)
        task2 = cv2.flip(img2, self.flipParameter)
        return task1,  task2

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img2 = Image.get_frame(img=self.secondImage, redis_db=self.redis_db)
        img.value = self.blurring(img.value)
        img.value = self.flipping(img.value)
        img2.value = self.blurring(img2.value)
        img2.value = self.flipping(img2.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        self.secondImage = Image.set_frame(img=img2, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_blurring(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()

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
from components.RotationExampleEnsar.src.utils.response import build_response
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel


class RotationExampleEnsar(Component):
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

    def rotation(self, img):
        return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    def gray(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.rotation(img.value)
        img.value = self.gray(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
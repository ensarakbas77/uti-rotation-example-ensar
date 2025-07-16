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
from components.RotationExampleEnsar.src.utils.response import build_response_brightness
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel


class BrightnessExampleEnsar(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.deneme = self.request.get_param("Deneme")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def brightness(self, img):
        alpha = 2.0
        beta = 100
        return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    def write(self, img):
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (100, 150)
        fontScale = 4
        color = (255, 0, 0)
        thickness = 4
        return cv2.putText(img, 'Ensar Deneme', org, font,
                            fontScale, color, thickness, cv2.LINE_AA)

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.brightness(img.value)
        img.value = self.write(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_brightness(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()


from sdks.novavision.src.helper.package import PackageHelper
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, RotationExampleEnsarExecuterOutputs, BrightnessExampleEnsarExecutorOutputs, RotationExampleEnsarExecuterResponse, BrightnessExampleEnsarExecutorResponse, RotationExampleEnsarExecuter, BrightnessExampleEnsarExecutor, OutputImage


def build_response_rotation(context):
    outputImage = OutputImage(value=context.image)
    outputs = RotationExampleEnsarExecuterOutputs(outputImage=outputImage)
    rotationExampleEnsarExecuterResponse = RotationExampleEnsarExecuterResponse(outputs=outputs)
    rotationExampleEnsarExecuter = RotationExampleEnsarExecuter(value=rotationExampleEnsarExecuterResponse)
    executor = ConfigExecutor(value = rotationExampleEnsarExecuter)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


def build_response_brightness(context):
    outputImage = OutputImage(value=context.image)
    outputs = BrightnessExampleEnsarExecutorOutputs(outputImage=outputImage)
    brightnessExampleEnsarExecutorResponse = BrightnessExampleEnsarExecutorResponse(outputs=outputs)
    brightnessExampleEnsarExecutor = BrightnessExampleEnsarExecutor(value=brightnessExampleEnsarExecutorResponse)
    executor = ConfigExecutor(value=brightnessExampleEnsarExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

from sdks.novavision.src.helper.package import PackageHelper
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, RotationExampleEnsarExecuterOutputs, BrightnessExampleEnsarExecutorOutputs, BlurringExampleEnsarExecutorOutputs, RotationExampleEnsarExecuterResponse, BrightnessExampleEnsarExecutorResponse, BlurringExampleEnsarExecutorResponse, RotationExampleEnsarExecuter, BrightnessExampleEnsarExecutor, BlurringExampleEnsarExecutor, OutputImage


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

def build_response_blurring(context):
    outputImage = OutputImage(value=context.image)
    outputs = BlurringExampleEnsarExecutorOutputs(outputImage=outputImage)
    blurringExampleEnsarExecutorResponse = BlurringExampleEnsarExecutorResponse(outputs=outputs)
    blurringExampleEnsarExecutor = BlurringExampleEnsarExecutor(value=blurringExampleEnsarExecutorResponse)
    executor = ConfigExecutor(value=blurringExampleEnsarExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
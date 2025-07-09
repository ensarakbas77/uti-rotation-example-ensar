
from sdks.novavision.src.helper.package import PackageHelper
from components.RotationExampleEnsar.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, RotationExampleEnsarExecuterOutputs, RotationExampleEnsarExecuterResponse, RotationExampleEnsarExecuter, OutputImage


def build_response(context):
    outputImage = OutputImage(value=context.image)
    outputs = RotationExampleEnsarExecuterOutputs(outputImage=outputImage)
    rotationExampleEnsarExecuterResponse = RotationExampleEnsarExecuterResponse(outputs=outputs)
    rotationExampleEnsarExecuter = RotationExampleEnsarExecuter(value=rotationExampleEnsarExecuterResponse)
    executor = ConfigExecutor(value = rotationExampleEnsarExecuter)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
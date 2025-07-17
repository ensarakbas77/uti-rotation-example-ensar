from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, \
    Config


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class InputSecondImage(Input):
    name: Literal["inputSecondImage"] = "inputSecondImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputSecondImage(Output):
    name: Literal["outputSecondImage"] = "outputSecondImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class KeepSideFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class KeepSideTrue(Config):
    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class KeepSideBBox(Config):
    """
        Rotate image without catting off sides.
    """
    name: Literal["KeepSide"] = "KeepSide"
    value: Union[KeepSideTrue, KeepSideFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Keep Sides"


class Degree(Config):
    """
        Positive angles specify counterclockwise rotation while negative angles indicate clockwise rotation.
    """
    name: Literal["Degree"] = "Degree"
    value: int = Field(ge=-359.0, le=359.0, default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Angle"


class FlipParameter(Config):
    """
        Enter the value for the flipping operation. (1--> Horizontal , 0--> Vertical, -1--> Horizontal & Vertical)
    """
    name: Literal["flipParameter"] = "flipParameter"
    value: int = Field(ge=-1, le=1, default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["integers between [-1, 1]"] = "integers between [-1, 1]"

    class Config:
        title = "Flipping Value"


class TextWrite(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Text Write"


class BrightnessBeta(Config):
    name: Literal["True"] = "True"
    value: int = Field(ge=0, le=100, default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["beta value"] = "beta value"

    class Config:
        title = "Brightness"


class BrightnessTextWrite(Config):
    """
        Brightness or Text Write section
    """
    name: Literal["brightnessTextWrite"] = "brightnessTextWrite"
    value: Union[BrightnessBeta, TextWrite]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Brightness or Text Write"



class BlurringExampleEnsarExecutorInputs(Inputs):
    inputImage: InputImage
    inputSecondImage: InputSecondImage


class BlurringExampleEnsarExecutorConfigs(Configs):
    degree: Degree
    drawBBox: KeepSideBBox
    flipParameter: FlipParameter


class BlurringExampleEnsarExecutorRequest(Request):
    inputs: Optional[BlurringExampleEnsarExecutorInputs]
    configs: BlurringExampleEnsarExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class BlurringExampleEnsarExecutorOutputs(Outputs):
    outputImage: OutputImage
    outputSecondImage: OutputSecondImage


class BlurringExampleEnsarExecutorResponse(Response):
    outputs: BlurringExampleEnsarExecutorOutputs


class BlurringExampleEnsarExecutor(Config):
    name: Literal["BlurringExampleEnsar"] = "BlurringExampleEnsar"
    value: Union[BlurringExampleEnsarExecutorRequest, BlurringExampleEnsarExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Blurring and Flipping"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class BrightnessExampleEnsarExecutorInputs(Inputs):
    inputImage: InputImage


class BrightnessExampleEnsarExecutorConfigs(Configs):
    degree: Degree
    drawBBox: KeepSideBBox
    brightnessTextWrite: BrightnessTextWrite


class BrightnessExampleEnsarExecutorRequest(Request):
    inputs: Optional[BrightnessExampleEnsarExecutorInputs]
    configs: BrightnessExampleEnsarExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class BrightnessExampleEnsarExecutorOutputs(Outputs):
    outputImage: OutputImage


class BrightnessExampleEnsarExecutorResponse(Response):
    outputs: BrightnessExampleEnsarExecutorOutputs


class BrightnessExampleEnsarExecutor(Config):
    name: Literal["BrightnessExampleEnsar"] = "BrightnessExampleEnsar"
    value: Union[BrightnessExampleEnsarExecutorRequest, BrightnessExampleEnsarExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Brightness and Text"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class RotationExampleEnsarExecuterInputs(Inputs):
    inputImage: InputImage


class RotationExampleEnsarExecuterConfigs(Configs):
    degree: Degree
    drawBBox: KeepSideBBox


class RotationExampleEnsarExecuterRequest(Request):
    inputs: Optional[RotationExampleEnsarExecuterInputs]
    configs: RotationExampleEnsarExecuterConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class RotationExampleEnsarExecuterOutputs(Outputs):
    outputImage: OutputImage


class RotationExampleEnsarExecuterResponse(Response):
    outputs: RotationExampleEnsarExecuterOutputs


class RotationExampleEnsarExecuter(Config):
    name: Literal["RotationExampleEnsar"] = "RotationExampleEnsar"
    value: Union[RotationExampleEnsarExecuterRequest, RotationExampleEnsarExecuterResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Rotation and GrayScaling"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[RotationExampleEnsarExecuter, BrightnessExampleEnsarExecutor, BlurringExampleEnsarExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["RotationExampleEnsar"] = "RotationExampleEnsar"
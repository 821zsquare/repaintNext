from importlib import import_module

from . import sd2_sr
from .inpainting import load_inpainting_model, pre_download_inpainting_models

__all__ = ["sd2_sr", "sam", "load_inpainting_model", "pre_download_inpainting_models"]


def __getattr__(name):
    if name == "sam":
        return import_module(".sam", __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

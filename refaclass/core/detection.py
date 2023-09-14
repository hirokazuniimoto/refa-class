import abc

from refaclass.base import ClassName, classSource
from refaclass.core.outliers import AbstractOutliersDetectionMethod


class AbstractDetector(abc.ABC):
    @abc.abstractmethod
    def detect_violation_methods(self, class_source: classSource):
        pass


class SingleResponsibilityPrincipleDetector(AbstractDetector):
    """A detector that returns a single response for a given input."""

    def __init__(
        self,
        refaclass_settings,
        outliers_detection_methods: AbstractOutliersDetectionMethod,
    ):
        self.refaclass_settings = refaclass_settings
        self.outliers_detection_methods = outliers_detection_methods

    def detect_violation_methods(self, class_source: classSource):
        if self.refaclass_settings.is_ignore_class(class_source.class_name):
            return None

        methods = class_source.method_names

        outliers_methods = self.outliers_detection_methods.find_outliers(
            class_name=ClassName(class_source.class_name), methods=methods
        )

        return outliers_methods

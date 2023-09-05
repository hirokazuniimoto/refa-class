from refaclass.base import DetectViolationResults, classSource
from refaclass.core.detection import AbstractDetector
from refaclass.preprocess.class_handler import ClassHandler


class RefaclassExecutor:
    def run(self, source_codes, detector: AbstractDetector) -> DetectViolationResults:
        detect_violation_results = {}

        for source_code in source_codes:
            handler = ClassHandler(source_code)
            class_and_method_names = handler.get_class_and_method_name()

            for class_name, method_names in class_and_method_names.items():
                if not class_name:
                    continue

                if len(method_names) == 0:
                    continue

                class_source = classSource(
                    class_name=class_name, method_names=method_names
                )

                detect_outliers_methods = detector.detect_violation_methods(
                    class_source=class_source
                )

                if detect_outliers_methods is None:
                    continue

                if len(detect_outliers_methods) > 0:
                    detect_violation_results[class_name] = {
                        "result": "NG",
                        "outliers_methods": detect_outliers_methods,
                    }
                elif len(detect_outliers_methods) == 0:
                    detect_violation_results[class_name] = {
                        "result": "OK",
                        "outliers_methods": detect_outliers_methods,
                    }

        return DetectViolationResults(results=detect_violation_results)

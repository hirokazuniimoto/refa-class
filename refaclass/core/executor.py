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
                class_source = classSource(
                    class_name=class_name, method_names=method_names
                )
                is_detect_violation, optimal_n_clusters = detector.detect_violation(
                    class_source=class_source
                )
                if is_detect_violation:
                    detect_violation_results[class_name] = {"result": "NG", "method_names": method_names, "violation_details": detector.violation_details(class_source=class_source, n_clusters=optimal_n_clusters)}
                else:
                    detect_violation_results[class_name] = {"result": "OK", "method_names": method_names}

        return DetectViolationResults(results=detect_violation_results)

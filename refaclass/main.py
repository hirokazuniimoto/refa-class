import argparse
import os
import warnings
from typing import Final

from refaclass.core.outliers import CosineSimilarityOutliersDetectionMethod

from .core.detection import SingleResponsibilityPrincipleDetector
from .core.executor import RefaclassExecutor
from .core.model import FastTextModel
from .core.relation import VectorRelation
from .output.outputs import CsvOutput, TerminalOutput
from .preprocess.argument_handler import ArgumentHandler
from .preprocess.source_code_reader import sourceCodeReader
from .settings import RefaclassSettings

warnings.simplefilter("ignore", FutureWarning)


# ライブラリがインストールされているディレクトリを取得
LIBRARY_DIR: Final = os.path.dirname(os.path.abspath(__file__))


def main(
    args: ArgumentHandler = ArgumentHandler(parser=argparse.ArgumentParser()),
) -> None:
    # preprocessing
    reader = sourceCodeReader(dir=args.dir)
    source_codes = reader.get_source_codes()

    # core
    executor = RefaclassExecutor()
    detect_violation_results = executor.run(
        source_codes=source_codes,
        detector=SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(),
            outliers_detection_methods=CosineSimilarityOutliersDetectionMethod(
                model=FastTextModel(lib_dir=LIBRARY_DIR),
                relation=VectorRelation(),
                threshold=float(args.threshold) if args.threshold is not None else 0.5,
            ),
        ),
    )

    # output
    output = args.output
    if output == "csv":
        detect_violation_results.output(output=CsvOutput())
    elif output == "terminal":
        detect_violation_results.output(output=TerminalOutput())
    else:
        detect_violation_results.output(output=TerminalOutput())


if __name__ == "__main__":
    main(args=ArgumentHandler(parser=argparse.ArgumentParser()))

import argparse

from .core.clustering import KMeansClusteringMethod
from .core.detection import SingleResponsibilityPrincipleDetector
from .core.executor import RefaclassExecutor
from .core.model import FastTextModel
from .output.outputs import CsvOutput, TerminalOutput
from .preprocess.argument_handler import ArgumentHandler
from .preprocess.source_code_reader import sourceCodeReader
from .settings import RefaclassSettings


def main(args: list = None):
    # preprocessing
    reader = sourceCodeReader(dir=args.dir)
    source_codes = reader.get_source_codes()

    # core
    executor = RefaclassExecutor()
    detect_violation_results = executor.run(
        source_codes=source_codes,
        detector=SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(),
            clustering_method=KMeansClusteringMethod(model=FastTextModel()),
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
    args = ArgumentHandler(parser=argparse.ArgumentParser())
    main(args=args)

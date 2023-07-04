from .preprocess.class_handler import ClassHandler
from .preprocess.source_code_reader import sourceCodeReader


def main():
    reader = sourceCodeReader()
    source_codes = reader.get_source_codes()

    for source_code in source_codes:
        handler = ClassHandler(source_code)
        class_names = handler.get_class_and_method_name()

        # print class and method names respectively
        if class_names:
            for class_name, method_names in class_names.items():
                if class_name != "":  # if class name is empty, skip
                    print(class_name, method_names)


if __name__ == "__main__":
    main()

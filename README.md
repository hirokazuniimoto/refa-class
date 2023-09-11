[![<ORG_NAME>](https://circleci.com/gh/hirokazuniimoto/refa-class.svg?style=svg)](https://app.circleci.com/pipelines/github/hirokazuniimoto/refa-class)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/refaclass)
![PyPI - Version](https://img.shields.io/pypi/v/refaclass)
![PyPI - Format](https://img.shields.io/pypi/format/refaclass)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/hirokazuniimoto/refa-class/main)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/hirokazuniimoto/refa-class)
![PyPI - License](https://img.shields.io/pypi/l/refaclass)



# refa-class

`Single Responsibility Principle` checker

## Description

This library detects classes in your source code that may violate the Single Responsibility Principle. If a method does not exist in a class, that class is ignored.

## Getting Started

### Notice
* The first run will take some time as the model needs to be downloaded.

### Installing
* refa-class can be installed using pip:
    ```
    pip install refaclass
    ```

* local environment  
  If you want to run the code locally, or change or modify it, you can install from the repo directly:
  ```
  git clone https://github.com/hirokazuniimoto/refa-class.git  
  cd refa-class  
  pip install -r requirements.txt
  pip install -r requirements.dev.txt
  ```

  run in local environment
  
  ```
  python3 -m refaclass.main

  The following arguments are optional:
  -d --dir            directory path
  -o --output         output [terminal csv]
  -t --threshold      cosine similarity threshold between [method and method] [class and method] (detects below threshold) default: 0.5
  ```

  you can use [Visual Studio Code Dev Containers extension](https://code.visualstudio.com/docs/remote/containers) to create container

### Executing program

* you can check python `class` just like this:

  ```
  cd [project]
  refaclass

  The following arguments are optional:
    -d --dir            directory path
    -o --output         output [terminal csv]
    -t --threshold      cosine similarity threshold between [method and method] [class and method] (detects below threshold) default: 0.5
  ```

### Result

* `OK` Classes that are not considered to violate the Single Responsibility Principle
* `NG` Classes considered to violate the Single Responsibility Principle
  * Show detected methods

## Test

* run test
```
python -m unittest discover tests
```
* measure coverage
```
python -m coverage run -m unittest discover tests
python -m coverage report -m
```

## Setting File
This project utilizes configuration files `refaclass.ini` to customize its behavior and settings. Configuration files play a crucial role in tailoring the application to your specific needs. 

* File Location: The configuration files arelocated at the root of the project.

### Configuration Sections
* refaclass-[class name]
* refaclass-[file name]
* refaclass-[directory name]

you can also use regular expressions

### Configuration Parameters
* ignore_checks: if set to `True`,  ignore file or class specified in that section
* is_file: if set to `True` then the content of the section is considered a file (if set to `False` or no `is_file` parameters then class)
* is_dir: if set to `True` then the content of the section is considered a directory (if set to `False` or no `is_file` parameters then class)

### Example
```
[refaclass-test_.*.py]
is_file = True
ignore_checks = True

[refaclass-Test.*]
ignore_checks = True

[refaclass-tests/test_core.*]
is_dir = True
ignore_checks = True
```

## Author
[Hirokazu Niimoto](https://github.com/hirokazuniimoto)

## Version History

* 1.5.1
    * [GitHub](https://github.com/hirokazuniimoto/refa-class/releases/tag/1.5.1)
    * [PyPI](https://pypi.org/project/refaclass/1.5.1/)
* 2.2.1
    * [GitHub](https://github.com/hirokazuniimoto/refa-class/releases/tag/2.1.0)
    * [PyPI](https://pypi.org/project/refaclass/2.2.1/)

## License

This project is licensed under the MIT License - see the LICENSE file for details

<!-- ## Paper(not published yet)
* [オブジェクト指向ソフトウェア設計における単一責任の原則違反の検出手法の提案]() -->

## Reference paper
* [Design Principles and Design Patterns](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf)
* [機械学習を用いたメソッド抽出リファクタリングの推薦手法](https://sel.ist.osaka-u.ac.jp/lab-db/betuzuri/archive/956/956.pdf)
* [自然言語処理を用いたデータベーススキーマの再構成支援ツールの開発](https://www.jstage.jst.go.jp/article/jssst/39/2/39_2_29/_pdf/-char/ja)



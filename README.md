[![<ORG_NAME>](https://circleci.com/gh/hirokazuniimoto/refa-class.svg?style=svg)](https://app.circleci.com/pipelines/github/hirokazuniimoto/refa-class)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/refaclass)

# refa-class

`Single Responsibility Principle` checker

## Description

This library detects classes in your source code that may violate the "Single Responsibility Principle".

## Getting Started

### Dependencies

* Python 3.8 or higher

### Installing
* refa-class can be installed using pip:
    ```
    pip install refaclass
    ```

* test environment (dev version)  
  If you want to run the development version of refa-class, you can install from pypi test environment:  
    [refaclass · TestPyPI](https://test.pypi.org/project/refaclass/)
    ```
    pip install -i https://test.pypi.org/simple/ refaclass 
    ```

* local environment  
  If you want to run the code locally, or change or modify it, you can install from the repo directly:
  ```
  git clone https://github.com/hirokazuniimoto/refa-class.git    
  ```
  
  ```
  python3 -m refaclass.main

  The following arguments are optional:
  -d --dir            directory path
  -o --output         output [terminal csv]
  ```

  you can use remote containers extension to create container
  - install and setup remote-containers extension in vscode
  https://code.visualstudio.com/docs/remote/containers

### Executing program

* you can check python `class` just like this:

  ```
  cd [project]
  refaclass

  The following arguments are optional:
    -d --dir            directory path
    -o --output         output [terminal csv]
  ```

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

* File Location: The configuration files are typically located in the config directory at the root of the project.

### Configuration Sections
* refaclass-[class name]
* refaclass-[file name]

you can also use regular expressions

### Configuration Parameters
* ignore_checks: if set to `True`,  ignore file or class specified in that section
* is_file: if set to `True` then the content of the section is considered a file

you can also use regular expressions

### Example
```
[refaclass-test_.*.py]
is_file = True
ignore_checks = True

[refaclass-Test.*]
ignore_checks = True
```



## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

## Reference paper



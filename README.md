[![<ORG_NAME>](https://circleci.com/gh/hirokazuniimoto/refa-class.svg?style=svg)](https://app.circleci.com/pipelines/github/hirokazuniimoto/refa-class)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/refaclass)

# refa-class

Simple overview of use/purpose.

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

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
  you can use remote containers extension to create container 

  - install and setup remote-containers extension in vscode
  https://code.visualstudio.com/docs/remote/containers

  ```
  python3 -m refaclass.main

  The following arguments are optional:
  --dir            directory path
  ```

### Executing program

you can check python `class` just like this:
```
cd [project]
refaclass

The following arguments are optional:
  --dir            directory path
```

### Test

* run test
```
python -m unittest discover tests
```
* measure coverage
```
python -m coverage run -m unittest discover tests
python -m coverage report -m
```

### Settings


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



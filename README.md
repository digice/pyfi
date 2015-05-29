# PYFI #

[www.pyfiapp.com](http://www.pyfiapp.com/)

_A Python Mining App to Provide a Back End for Financial Data APIs_

###### AUTHOR: ######
Roderic Linguri [rlinguri@mac.com](mailto:rlinguri@mac.com)

###### DEPENDENCY: ######
This application requires the installation of [pyfwk](https://github.com/rlinguri/pyfwk)

![pyfwk](http://www.pyfiapp.com/img/pyfwk2.svg)

###### INSTALLATION INSTRUCTIONS: ######
Download the Zip file and unpack or clone the repository. In the commandline, navigate to the directory containing the setup.py file. At the prompt, type:

    python setup.py install
    
You should then be able to put

    import pyfi
    
into your module to import the framework.

###### REQUIRED METHOD: ######
You must set the root directory of your project in the FileManager utility:

    fm = pyfwk.FileManager.instance()
    fm.set_root('/absolute/path/to/your/project_root')

You can then create an Entity object by referring to its ID:

    entity = Entity(1123)
    print(json.dumps(entity.dict(), indent=4, sort_keys=True, separators=(',', ': ')))


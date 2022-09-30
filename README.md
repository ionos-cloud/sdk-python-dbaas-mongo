[![Gitter](https://img.shields.io/gitter/room/ionos-cloud/sdk-general)](https://gitter.im/ionos-cloud/sdk-general)
[![PyPI version](https://img.shields.io/pypi/v/ionoscloud-dbaas-mongo)](https://pypi.org/project/ionoscloud-dbaas-mongo/)

# ionoscloud
With IONOS Cloud Database as a Service, you have the ability to quickly set up and manage a MongoDB database. You can also delete clusters, manage backups and users via the API.

MongoDB is an open source, cross-platform, document-oriented database program. Classified as a NoSQL database program, it uses JSON-like documents with optional schemas.

The MongoDB API allows you to create additional database clusters or modify existing ones. Both tools, the Data Center Designer (DCD) and the API use the same concepts consistently and are well suited for smooth and intuitive use.

**Note:** DBaaS - MongoDB is currently in the **Early Access (EA)** phase. We recommend keeping usage and testing to non-production critical applications. Please contact your sales representative or support for more information.

## Requirements.

- Python >= 3.5

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-mongo.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python-dbaas-mongo.git`)

Then import the package:
```python
import ionoscloud_dbaas_mongo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ionoscloud_dbaas_mongo
```
## Our latest, most up to date documentation is available [here](https://github.com/ionos-cloud/ionos-cloud-sdk-python-dbaas-mongo/blob/master/README.md)

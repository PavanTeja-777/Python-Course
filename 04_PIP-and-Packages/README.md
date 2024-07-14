# PIP and Packages

## PIP

- PIP, which stands for "Pip Installs Packages," is a package management system used to install and manage software packages written in Python.

- It's a tool that downloades Libraries from Internet

Here are some key points about PIP.

1. Installation and Upgrading:

    - Install: You can install a package using PIP with the command pip install package-name.
    - Upgrade: To upgrade a package, you use pip install --upgrade package-name.

2. Uninstallation:

    - To uninstall a package, the command is pip uninstall package-name.

3. Listing Installed Packages:

    - You can list all installed packages with pip list.

4. Requirements Files:

    - PIP can install all dependencies listed in a requirements.txt file using pip install -r requirements.txt.

5. Virtual Environments:

    - PIP is often used in conjunction with virtual environments (created using venv or virtualenv) to manage dependencies for different projects separately.

6. Searching for Packages:

    - You can search for packages using pip search search-term.

7. Checking for Outdated Packages:

    - To see which packages are outdated, use pip list --outdated.

8. Freezing Dependencies:

    - To generate a requirements.txt file listing the current environment's dependencies, use pip freeze > requirements.txt.

## Packages a.k.a Libraries
In Python, a module is a file containing Python definitions and statements. Modules are used to organize code into manageable and reusable pieces.

Some of the most popular Libraries are:
- Flask: Lightweight WSGI web application framework for building simple and flexible web applications.

- Pygame: Set of Python modules designed for writing video games.

- NumPy:  Fundamental package for scientific computing with support for arrays and matrices.

- PyTorch:  Popular for deep learning, known for its dynamic computation graph and ease of use.

- BeautifulSoup:  Library for parsing HTML and XML documents and extracting data from them.

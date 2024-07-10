To create and activate a virtual environment using `pyenv` in Ubuntu, follow these steps:

### Step 1: Install `pyenv`

If you haven't installed `pyenv` yet, you can do so by following these steps:

1. **Update and install dependencies**:

    ```bash
    sudo apt update
    sudo apt install -y build-essential curl libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

2. **Install `pyenv`**:

    You can install `pyenv` using the recommended installation script.

    ```bash
    curl https://pyenv.run | bash
    ```

3. **Configure your shell**:

    Add the following lines to your shell startup file (`~/.bashrc`):

    ```bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

    After adding these lines, restart your shell:

    ```bash
    exec $SHELL
    ```

### Step 2: Install Python Version

Use `pyenv` to install the desired version of Python. For example, to install Python 3.10.12:

```bash
pyenv install 3.10.12
```

### Step 3: Create a Virtual Environment

Once you have the desired Python version installed, you can create a virtual environment using `pyenv virtualenv`.

```bash
pyenv virtualenv 3.10.12 test-env
```

Here, `3.10.12` is the version of Python you want to use, and `test-env` is the name of your virtual environment.

### Step 4: Activate the Virtual Environment

To activate the virtual environment, use the following command:

```bash
pyenv activate test-env
```

### Step 5: Verify the Virtual Environment

To verify that the virtual environment is activated, you can check the Python version:

```bash
python --version
```

It should display the Python version you specified for your virtual environment.

### Step 6: Deactivate the Virtual Environment

To deactivate the virtual environment, use the following command:

```bash
pyenv deactivate
```

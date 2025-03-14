# Cloud - Infrastructure as Code: AWS CLI & Terraform  

> Learning Goals
>- Infrastructure as Code
>- Understand and Install AWS CLI
>- Introduction of Terraform 
>- Install and create EC2 instances

**Last Session**

- Volumes:
    - to store persistent data
    - in containers are meant to store only non-persistent data: e.g. error logs from nginx
        - for this containers have thin writable layer
    - volumes are stored locally on the docker host
        - linux: /var/lib/docker/volumes/
    - how to show all volumes:
        `docker volumes ls`
    - how to display meta date of an volume:
        `docker inspect my_volume`
    - mount an volume into a container:
        `docker run -it --name MyContainer --mount source=newVol,target=/my_data ubuntu bash`

- CI/CD
    - Continuous Integration/ Continuous Delivery (Deploy)
    - `(django) unittest` are run after new code is pushed into a branch 
        - more commits per day
        - faster releases
        - improvement of code quality
    - tools:
        - github action (that we used yesterday)
        - jenkins
    - main.yml
        - we can name this github action file
        - we set a target branch; pushing to that branch started github action
            - we define the OS: `ubuntu-latest` --> VW
            - we can also define a service: e.g. postgres
                - services in github action are docker containers
            - then we gave the instructions (we label the with the `-name`)
                - installing a python env.
                - installing django dependencies
                - run migrations
                - finally: run the test

## AWS CLI

- aws cli is used to connect to AWS API
    - to connect and manage to aws service
        - e.g. start and destroy a ec2 instances
- install
- example commands

#### Install AWS CLI

### Step 1: Install `curl` and `unzip` (if not already installed)

First, ensure you have `curl` and `unzip` installed. These are required to download and extract the AWS CLI installation package:

```bash
sudo apt update
sudo apt install curl unzip less -y
```

### Step 2: Download the AWS CLI Installer

Use the following `curl` command to download the latest AWS CLI version 2 installation file for 64-bit systems:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

For ARM-based systems (like Raspberry Pi or AWS Graviton instances), download this instead:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
```

### Step 3: Unzip the Installer

Once the download is complete, unzip the file:

```bash
unzip awscliv2.zip
```

### Step 4: Run the Installer

Now, run the AWS CLI installer:

```bash
sudo ./aws/install
```

### Step 5: Verify the Installation

After the installation completes, check if the AWS CLI is installed correctly by running:

```bash
aws --version
```

You should see something like:

```bash
aws-cli/2.x.x Python/3.x.x Linux/Ubuntu
```

    
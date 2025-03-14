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

### Basic AWS CLI Commands

**Listing S3 Buckets:**

   This command lists all your S3 buckets.
   ```bash
   aws s3 ls
   ```

**Launching an EC2 instance:**

   This command starts an EC2 instance using a specified AMI ID and instance type.
```bash
aws ec2 run-instances --image-id ami-07eef52105e8a2059 --count 1 --instance-type t2.micro
```

**Describing all current ec2 instances:**

```bash
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId,State:State.Name}' --output table
```
- this returns us the instance id and the current state of each ec2

**Terminate/stop the EC2 Instance**

```bash
aws ec2 stop-instances --instance-ids i-xxxxxxxx
aws ec2 terminate-instances --instance-ids i-xxxxxxxx
```

**Listing available IAM users:**

   This command lists all IAM users in your AWS account.
   ```bash
   aws iam list-users
   ```

# Terraform

- A tool for provisioning and managing infrastructure as code (IaC),
- primarily for cloud-based environments

- **Infrastructure as Code (IaC)**:
    - Automates infrastructure provisioning using machine-readable definition files, replacing manual processes.  
- **Provisioning vs. Configuration Management (CM)**:
    - Terraform deploys infrastructure (Provisioning),
    - while CM tools manage application delivery / deployment, mainly on virtual machines (VMs e.g. ec2)
        - Ansible, Puppet, SaltStack, Chef
    -  **Key Benefits**: 
        - human-readable configuration code is defined
        - configuration code deploy, and manage repeatable and consistent environments across public, private, and hybrid clouds.
        - Terraform can deploy infrastructure to any cloud or combination of clouds.

**What makes Terraform to stand out**

Many other tools exist,
- AWS (CloudFormation), 
- Microsoft (ARM), and 
- Google (Deployment Manager)

- Easy to use
- Free and open source
- Declarative—Say what you want, not how to do it.
- Cloud-agnostic - Deploy to any cloud using the same tool.
- Expressive and extendable — You aren’t limited by the language.

## **Terraform vs. CM Tools**
- **Key Philosophical Difference**
    - **CM Tools → Mutable Infrastructure**: Updates are applied to existing servers.
    - **Provisioning Tools (Terraform) → Immutable Infrastructure**: Treats infrastructure as disposable, replacing instead of modifying. 
    - **Mindset Shift**: Mutable infrastructure is **reusable**,
    while immutable infrastructure is **disposable**

## Declarative programming

- **Declarative Programming**: 
    - Specifies **what** the outcome should be without defining step-by-step instructions.
- **Examples**:
    - **SQL** (queries specify what data is needed, not how to retrieve it).
    - **IaC tools** (Terraform, Ansible, Chef, Puppet) define desired infrastructure states.  
    - **Configuration languages** (XML, JSON) structure data without control flow logic. 
- **Declarative** → Focuses on the **end goal** (destination).  
- **Imperative** → Focuses on the **process** (journey). 

**Benefits**
- **consistency**
- **Idempotency**
- **Scalability**
- **Automation-friendly e.g. CI/CD**
 
## Install Terraform

- Terraform **0.15.X** installed ([Installation Guide](https://learn.hashicorp.com/terraform/getting-started/install.html)).

### Verify the installation
After the installation is complete, verify that Terraform is installed correctly by checking the version:

```bash
terraform -v
```

### 1.2.1 Writing the Terraform configuration

- **Terraform Configuration Files**: Terraform reads `.tf` files to deploy infrastructure.  
- **Defining Infrastructure as Code**:  
  - Declare an **EC2 instance** in a `.tf` file.  
  - Use **main.tf** as the primary configuration file.  
- **Terraform File Processing**:  
  - Reads **all `.tf` files** in the working directory.  
  - **Concatenates** them into a single configuration.  
- **Next Step**: Create `main.tf` and define an EC2 instance in Terraform code.

```bash
resource "aws_instance" "helloworld" {  # [1] Resource block defining an EC2 instance
    ami           = "ami-07eef52105e8a2059"  # [2] Specify the Amazon Machine Image (AMI)
    instance_type = "t2.micro"  # [2] Define the instance type

    tags = {  # [2] Assign a tag to the instance
        Name = "HelloWorld"
    }
}

```

1. Declares an aws_instance resource with name “HelloWorld”
2. Attributes for the EC2 instance


- **Terraform Resources**: Core elements in Terraform that **provision infrastructure** (e.g., VMs, load balancers, NAT gateways).  
- **Resource Declaration**:  
  - Defined using **HCL objects** with the `resource` keyword.  
  - Requires **two labels**:  
    1. **Resource Type** (e.g., `aws_instance`, `aws_s3_bucket`).  
    2. **Resource Name** (user-defined, used for internal reference).  
- **Resource Identifier**:  
  - Combination of **type + name** (e.g., `aws_instance.helloworld`).  
  - **Uniqueness**: Must be unique within the module scope.  
- **No External Significance**: The resource name is only used within Terraform to **reference resources**, not in AWS.  

- **Terraform Resources Have Inputs & Outputs**:  
  - **Inputs → Arguments**: User-defined values passed to the resource.  
  - **Outputs → Attributes**: Properties exposed by the resource after creation.  

- **Types of Attributes**:  
  1. **Regular Attributes**: Derived from arguments and accessible after creation.  
  2. **Computed Attributes**: after the resource is created (e.g., **public IP**, **DNS name**).  

- **Example (`aws_instance`)**:  
  - **Arguments (Inputs)**: `ami`, `instance_type`, `tags`, etc.  
  - **Regular Attributes**: `id`, `arn`, etc. (available immediately).  
  - **Computed Attributes**: `public_ip`, `private_dns`, etc. (only available after provisioning).  


# -------- distinction between arguments, attributes, and computed attributes

### 1.2.2 Configuring the AWS provider

### **Configuring the AWS Provider in Terraform**  

- **What is the AWS Provider?**  
  - Handles **API interactions** with AWS.  
  - Makes **authenticated requests** to AWS services.  
  - Exposes AWS resources to **Terraform**.  

- **Provider Configuration**  
  - The `provider` block **specifies which cloud/service Terraform will interact with**.  
  - Defines **region**, **authentication**, and other settings.  

### **Example AWS Provider Block**  
```hcl
provider "aws" {
  region = "us-east-1"  # Set AWS region
}
```
  
- **Authentication**  
  - Terraform uses **AWS credentials** via **shared credentials file** generated by **aws cli**.  
- With the provider configured, Terraform can now authenticate and provision AWS resources. 🚀 Update your code in main.tf as shown next.

main.tf

```bash
provider "aws" { 
  region = "eu-central-1"  
}

resource "aws_instance" "helloworld" { 
  ami           = "ami-09dd2e08d601bfF67"  
  instance_type = "t2.micro"

  tags = { 
    Name = "HelloWorld"
  }
}

```

1. Declares the AWS provider
2. Configures a deployment region

NOTE You will need to obtain AWS credentials before you can provision infrastructure. These can be stored either in the credentials file


- **Providers vs. Resources**:  
  - **Resources** → Require **two labels**: **Type** & **Name** (e.g., `aws_instance.helloworld`).  
  - **Providers** → Require **only one label**: **Provider Name** (e.g., `"aws"`, `"google"`, `"azurerm"`).  

- **Provider Naming**:  
  - Must match the **official name** in the **Terraform Registry**.  
  - Examples:  
    - **AWS** → `"aws"`  
    - **Google Cloud** → `"google"`  
    - **Azure** → `"azurerm"`  

- **Purpose of Providers**:  
  - Enable **Terraform to communicate with cloud APIs**.  
  - Handle **authentication & API requests**.  
  - Expose **resources Terraform can manage**.  

- **Key Rule**: A Terraform configuration can include **multiple providers** if managing resources across different cloud services.

- **Terraform Registry**:  
  - A **global repository** for storing and sharing **versioned provider binaries**.  
  - Terraform **automatically downloads required providers** during initialization (`terraform init`).  

- **Providers Only Have Inputs (No Outputs)**:  
  - Unlike resources, **providers do not return outputs**.  
  - They only accept **configuration arguments** to define how Terraform interacts with external APIs.  

- **Provider Configuration Arguments**:  
  - **Service Endpoint URL**: Defines API communication points.  
  - **Region**: Specifies which cloud region to operate in.  
  - **Provider Version**: Ensures a specific provider version is used.  
 
  
- **Key Takeaway**: Terraform **automates provider management** through the **Terraform Registry**, allowing seamless updates and consistent infrastructure provisioning.

# ----- API call via Terraform

### 1.2.3 Initializing Terraform
### **Initializing Terraform Workspace**  

- **Why Initialization is Required?**  
  - Terraform **downloads** and **installs** the required **provider binaries** (e.g., AWS, GCP) from the **Terraform Registry**.  
  - Ensures **all dependencies** are correctly set up before applying configurations.  
  - Required **at least once per workspace** before Terraform can deploy resources.  

- **Command to Initialize Terraform**:  
  ```sh
  terraform init
  ```

- **Expected Output (Example)**:  
```bash
  Initializing the backend...
  
  Initializing provider plugins...
  - Finding latest version of hashicorp/aws...
  - Installing hashicorp/aws v4.35.0...
  - Installed hashicorp/aws v4.35.0 (signed by HashiCorp)
  
  Terraform has been successfully initialized!
  ```
1. Terraform fetches the latest version of the AWS provider.
2. The only thing we really care about

- **What Happens During Initialization?**  
  - **Configures the backend** (e.g., local state file or remote storage like S3).  
  - **Downloads provider plugins** (e.g., AWS, GCP, Azure).  
  - **Verifies provider versions** based on `provider` block.  
  - **Prepares Terraform to run other commands** (e.g., `terraform plan`, `terraform apply`).  





#### 1.2.4 Deploying the EC2 instance 
### **Deploying the EC2 Instance with Terraform**  

#### **1. Run the Apply Command**
```bash
terraform apply
```

#### **2. Execution Plan Overview**  
- Terraform generates an **execution plan**, outlining the **changes it will make** to match the desired state.  
- The plan helps **verify** that the configuration is correct before applying it.  
- Example output snippet (before approval):  
  ```
  An execution plan has been generated and is shown below.
  Resource actions are indicated with the following symbols:
    + create

  Terraform will perform the following actions:

    # aws_instance.helloworld will be created
    + resource "aws_instance" "helloworld" {
        + ami           = "ami-09dd2e08d601bfF67"
        + instance_type = "t2.micro"
        + tags          = {
            + Name = "HelloWorld"
          }
      }

  Do you want to perform these actions?  
    Terraform will create these resources.  
    Enter a value:  
  ```
#### **3. Review & Approve the Plan**
- If everything looks correct, type **`yes`** and press **Enter** to proceed.  

#### **4. Terraform Applies the Changes**  
- Terraform provisions the EC2 instance (typically takes 1-2 minutes).  
- Expected **successful deployment output**:  
```bash
  aws_instance.helloworld: Creating...
  aws_instance.helloworld: Still creating... [10s elapsed]
  aws_instance.helloworld: Still creating... [30s elapsed]
  aws_instance.helloworld: Creation complete after 1m 15s
  
  Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
  ```

#### **5. Verify the Deployment**
- Retrieve details about the deployed EC2 instance:
  ```bash
  terraform show
  ```
- Check the AWS Management Console to confirm the instance is running.  


### 1.2.5 Destroying the EC2 instance

### **Destroying the EC2 Instance with Terraform**  

#### **1. Why Destroy Resources?**  
- **Cost Management**: Running AWS instances incurs charges.  
- **Best Practice**: Always clean up unused infrastructure.  

#### **2. Command to Destroy Resources**  
```bash
terraform destroy
```

#### **3. Execution Plan Overview**  
- Terraform first **refreshes the state** to check the current status.  
- Displays a **destroy plan** similar to `terraform apply`, but for deletion.  
- Example output before confirmation:  
  ```
  aws_instance.helloworld: Refreshing state... [id=i-070098fcf77d93c54]
  Terraform used the selected providers to generate the following execution plan.
  Resource actions are indicated with the following symbols:
  
  - destroy
  
  Terraform will perform the following actions:

  # aws_instance.helloworld will be destroyed
  - resource "aws_instance" "helloworld" {
      id = "i-070098fcf77d93c54"
    }

  Do you really want to destroy all resources?  
    Terraform will delete these resources.  
    Enter a value:
  ```
#### **4. Confirm the Destruction**  
- **Type `yes`** and press **Enter** to proceed.  

#### **5. Terraform Executes the Deletion**  
- Expected output during destruction:  
  ```
  aws_instance.helloworld: Destroying... [id=i-070098fcf77d93c54]
  aws_instance.helloworld: Still destroying... [10s elapsed]
  aws_instance.helloworld: Still destroying... [20s elapsed]
  aws_instance.helloworld: Still destroying... [30s elapsed]
  aws_instance.helloworld: Destruction complete after 31s
  ```
- Final confirmation:  
  ```
  Destroy complete! Resources: 1 destroyed.
  ```

#### **6. Verify Resource Deletion**  
- Refresh the **AWS Console** to check if the instance is gone.  
- Run:
  ```bash
  terraform show
  ```
  - If everything was deleted, it will return **nothing**.


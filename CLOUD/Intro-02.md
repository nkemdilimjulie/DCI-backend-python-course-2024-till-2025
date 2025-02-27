# Cloud - Introduction - 02: Cloud and ec2

> Learning Goals
>- Serverless
>- Scalability and Elasticity
>- ec2 on aws
>- learn how to lunch, stop and terminate an ec2 instance


**Last Session**

- Cloud: They are servers and therefore, Computers
- cloud provider have entire data centers with lots of computers

- on-premise vs. cloud computing
    - on-premise means you buy your hardware
    1. you can have either over-provisioning
        - meaning having more resources than necessary
    2. or you have not enough computer power than necessary for your application
    3. you need capital for creating on-premise computing

- cloud fixes that for us:
    - by virtualization
        - using virtual machines
        - we have huge compute power from one machine in data centers
        - these machines are used to create VMs 
            - VMs simulate hardware with a fraction of the computer power of the host machine
- the consequence is to have a wide range of configuration settings demanded by the client
    - and accomplished by virtualization

- since we don't need capital and we only pay  resources we need and only for thee time we are using the cloud
    - cloud computing is more cost efficient than building on-premises datacenters

- but you have to be careful in which country you deploy your code, because of different data protection laws
 and aws operates world wide

- metered payment model or pay-as-you-go: only pay  resources we need and only for thee time we are using the cloud


- we have 3 different Platform Models:
    1. IaaS
        - provide hardware for example for you server/ec2 
            - we have to decide:
                1. which network: VPC, subnet
                2. amount of cores
                3. storage
                4. security groups
                5. tenancy
            - `shared responsibility model`
    2. PaaS
        - via an interface the system setup is less complex
        - here we focus only on out software
        - here we are only responsible for our application code
    3. SaaS
        - for end user 
        - no responsibilities at all

### Serverless Workloads

- cloud providers can also enable entirely new ways to administrate applications and data.
- Perhaps the most obvious example is serverless computing.

- but you can’t run a compute function without a computer environment (a “server”) somewhere that'll host it.
- What “serverless” does allow is for individual developers to run their code for seconds or minutes at
a time on some else’s cloud servers.

- The serverless model—as provided by services like `AWS Lambda`—
    - makes it possible to design code that reacts to external events. 
- When, for instance, a video file is uploaded to a repository
    - it can trigger a Lambda function that will convert the file to a new video format. 
- Theres no need to maintain and pay for an actual instance running 24/7,
- there’s no administration overhead to worry about.


### Scalability and Elasticity

#### 1. Scalability

- A scalable service will automatically grow in capacity to seamlessly meet any changes
in demand. 

- A well-designed cloud-based operation will constantly monitor the health
of its application stack and respond whenever preset performance metrics might soon go unmet.

- The response might include automatically launching new server instances
to add extra compute power to your existing cluster. 

- for example it can handle the capacity stresses required to keep millions
of Netflix customers happy

#### 2. Elasticity

AWS services:
1. Elastic Compute Cloud
2. Elastic Load Balancing
3. Elastic Beanstalk
and so on

- the term elastic is used because those services are built to be easily and automatically resized.
- Generally, you set the maximum and minimum performance levels you want for your application,
- and the AWS service(s) you're using will automatically add or remove resources to meet changing usage demands.
- a scalable e-commerce website could be configured to function using just a single server during
low-demand periods, but any number of additional servers could be automatically
brought online as demand spikes.
- When demand drops back down, unused servers will be shut down automatically.

## EC2 Elastic Compute Cloud

- ec2 instance are servers where we can deploy to

**Features of EC**

- **Scalability**: You can easily scale your infrastructure to match the needs of your application, ensuring that you are not overpaying for unused capacity.
- **Flexibility**: EC2 supports multiple operating systems (Windows, Linux, etc)
- **Elasticity**: EC2 allows for elastic scaling up or down, automatically responding to changes in traffic or workload.
- **Global Infrastructure**: With data centers across the world, EC2 offers low-latency connections, letting you deploy resources closest to your customers.
- **Cost Efficiency**: You can choose various pricing models such as on-demand, reserved instances, or spot instances, 
    - giving you the flexibility to manage costs effectively.

### Launching an EC2 Instance: Step-by-Step
Now, let’s walk through how to **launch an EC2 instance** and run a basic Nginx web server using a simple startup script.

#### **Step 1: Log in to AWS Management Console**
- Navigate to the **EC2 Dashboard** from the AWS console.

#### **Step 2: Launch an Instance**
- Click on **Launch Instance** and choose an **AMI (Amazon Machine Image)** such as **Ubuntu** 
- Choose the instance type, such as **t2.micro**, which is free-tier eligible.

#### **Step 3: Configure Instance Details**
- In the "Configure Instance" section, ensure the **VPC (Virtual Private Cloud)** and **subnet** are set correctly.
- Scroll to the bottom to the **Advanced Details** section, and here is where you’ll input your **user-data script** to automate the configuration.

#### **Step 4: Add Your Script (User Data)**
In the **User Data** field, paste the following script to install Nginx and set up a "Hello World" landing page:

```bash
#!/bin/bash
sudo apt update -y
sudo apt install nginx -y
echo "<h1>Hello World from Nginx on EC2!</h1>" | sudo tee /var/www/html/index.nginx-debian.html
sudo systemctl start nginx
sudo systemctl enable nginx
```

This script will automatically install and start Nginx, and display "Hello World" on your landing page.

#### **Step 5: Configure Security Group**
Ensure that your **security group** allows inbound traffic on **port 80 (HTTP)** and **port 22 (SSH)** so that you can access the Nginx server and SSH into the instance.

#### **Step 6: Review and Launch**
- Review your settings and click **Launch**.
- After the instance launches, you can visit its **public IP address** in a web browser, and you should see the "Hello World from Nginx on EC2!" page.




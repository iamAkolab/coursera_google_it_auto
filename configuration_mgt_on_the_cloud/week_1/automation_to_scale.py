#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Automating with Configuration Management

# Being able to automate the installation of new software, the provisioning of new workstations or the configuration of a new server can make a big difference 
# even when you're the only person in your IT departmentlike what we mean when we talk about scale and how we can use configuration management to maintain the 
# computers in our fleet, and how we can all benefit from treating our infrastructure as code. These concepts are the building blocks for letting us manage a 
# growing number of devices without having to grow the team in charge of them. 
# We'll then get to our first taste of Puppet, the configuration management tool 
# that we'll be teaching you throughout this course. We'll check out a bunch of different examples to see what Puppet rules look like. We'll also learn about 
# the underlying concepts and how you can get it to do the heavy lifting for yo

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is scale?

'''
Being able to scale what we do means that we can keep achieving larger impacts with the same amount of effort when a system scales. Well an increase in the amount of work it 
needs to do can be accommodated by an increase in capacity. For example, if the web application your company provides is scalable, that it can handle an increase in the number 
of people using it by adding more servers to serve requests. In short, a scalable system is a flexible one. Adding more computers to the pool of servers that are serving the 
website can be a very simple or very hard operation depending on how your infrastructure is set up. To figure out how scalable your current setup is, you can ask yourself 
questions like will adding more servers increase the capacity of the service? How are new servers prepared, installed, and configured? How quickly can you set up new computers 
to get them ready to be used? Could you deploy a hundred servers with the same IT team that you have today? Or would you need to hire more people to get it done faster? Would 
all the deployed servers be configured exactly the same way? Scaling isn't just about website serving content of course. If your company is rapidly hiring a lot of new employees, 
you'll need to have an onboarding process that can scale as needed. And as you keep adding new computers to the network, you'll need to make sure that your system administration 
process can scale to the growing needs of the company. This can include tasks like a applying the latest security policies and patches while making sure users' needs still get 
addressed all while more and more users join the network without new support staff to back you up. 
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is configuration management?
'''
By manually deploying the installation and configuring the computer, we see that we're using unmanaged configuration. 
When we say configuration here, we're talking about everything from the current operating system and the applications installed to any necessary configuration files or policies,
including anything else that's relevant for the server to do its job. When you work in IT, you're generally in charge of the configuration of a lot of different devices, not just
servers. Network routers printers and even smart home devices can have configuration that we can control. For example, a network switch might use a config file to set up each of
its ports. All right, so now we know what we mean when we talk about configuration. We said that manually deploying a server means that the configuration is unmanaged. So what 
would it mean for the configuration to be managed? It means using a configuration management system to handle all of the configuration of the devices in your fleet, also known 
as nodes. There's a bunch of different tools available depending on the devices and services involved. Typically you'll define a set of rules that have to be applied to the 
nodes you want to manage and then have a process that ensures that those settings are true on each of the nodes. At a small scale, unmanaged configurations seem inexpensive. 
If you only manage a handful of servers, you might be able to get away with doing that without the help of automation. You could log into each device and make changes by hand 
when necessary. And when your company needs a new database server, you might just go ahead and manually install the OS and the database software into a spare computer. 
But this approach doesn't always scale well. The more servers that you need to deploy, the more time it will take you to do it manually. And when things go wrong, and they 
often do, it can take a lot of time to recover and have the servers back online. Configuration management systems aim to solve this scaling problem. By managing the 
configuration of a fleet with a system like this, large deployments become easier to work with because the system will deploy the configuration automatically no matter how
many devices you're managing. When you use configuration management and you need to make a change in one or more computers, you don't manually connect to each computer to 
perform operations on it. Instead, you edit the configuration management rules and then let the automation apply those rules in the affected machines. 
This way the changes you make to a system or group of systems are done in a systematic, repeatable way. Being repeatable is important because it means that the results will 
be the same on all the devices. A configuration management tool can take the rules you define and apply them to the systems that it manages, making changes efficient and 
consistent. Configuration management systems often also have some form of automatic error correction built in so that they can recover from certain types of errors all by 
themselves. For example, say you found that some application that was being used widely in your company was configured to be very insecure. You can add rules to your 
configuration management system to improve the settings on all computers. And this won't just apply the more secure settings once. It will continue to monitor the 
configuration going forward. If a user changes the settings on their machine, the configuration management tooling will detect this change and reapply the settings you 
defined in code. How cool is that? 

There are lots of configuration management systems available in the IT industry today. Some popular systems include Puppet, Chef, Ansible, and CFEngine. These tools can be 
used to manage locally hosted infrastructure. Think bare metal or virtual machines, like the laptops or work stations that employees use at a company. Many also have some 
kind of Cloud integration allowing them to manage resources in Cloud environments like Amazon EC2, Microsoft Azure, or the Google Cloud platform, and the list doesn't stop 
there. There are some platform specific tools, like SCCM and Group Policy for Windows. These tools can be very useful in some specific environments, even when they aren't as 
flexible as the others. For this course, we've chosen to focus on Puppet because it's the current industry standard for configuration management. Keep in mind though that 
selecting a configuration management system is a lot like deciding on a programming language or version control system. 
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is infrastructure as code?

'''

We've called out that when we use a configuration management system, we write rules that describe how the computers in our fleet should be configured. These rules are then 
executed by the automation, to make the computers match our desired state. This means that we can model the behavior of our IT infrastructure in files that can be processed 
by automatic tools. These files can then be tracked in a version control system

The paradigm of storing all the configuration for the managed devices in version controlled files is known as Infrastructure as Code or IaC.
 In other words, we see that we're using Infrastructure as Code when all of the configuration necessary to deploy and manage a node in the infrastructure is stored in version control.
 This is then combined with automatic tooling to actually get the nodes provisioned and managed. If you have all the details of your Infrastructure properly stored in the system, 
 you can very quickly deploy a new device if something breaks down. Simply get a new machine, either virtual or physical, use the automation to deploy the necessary configuration,
 and you're done. The principals of Infrastructure as Code are commonly applied in cloud computing environments, where machines are treated like interchangeable resources, instead 
 of individual computers. This principle is also known as treating your computers as cattle instead of pets because you care for them as a group rather than individually
 
 One valuable benefit of this process is that the configuration applied to the device doesn't depend on a human remembering to follow all the necessary steps. Rest assured, silly 
 human, the result will always be the same, making the deployment consistent. As mentioned, having Infrastructure as Code means that we can also apply the benefits of the version
 control system or VCS to your infrastructure. Since the configuration of our computers is stored in files, those files can be added to a VCS. This has all the benefits that version
 control systems bring. It gives us an audit trail of changes, it lets us quickly rollback if a change was wrong, it lets others reviewed our code to catch errors and distribute 
 knowledge, it improves collaboration with the rest of the team, and it lets us easily check out the state of our infrastructure by looking at the rules that are committed
 Having your infrastructure stored as code means that you can automatically deploy your infrastructure with very little overhead. If you need to move it to a different location,
 it can be deployed, de-provisioned, and redeployed at scale in a different locale with minimal code level changes. 
 
 To sum all of this up, managing your Infrastructure as Code it means that your fleet of nodes are consistent, versioned, reliable, and repeatable. Instead of being seen as 
 precious or unique, machines are treated as replaceable resources that can be deployed on-demand through the automation. Any infrastructure that claims to be scalable must be 
 able to handle the capacity requirements of growth. Performing an action like adding more servers to handle an increase in requests is just a possible first step. There are 
 other things that we might need to take into account, such as the amount of traffic that network can handle or the load on the back end servers like databases. Viewing your 
 infrastructure in this way helps your IT team adapt and stay flexible. The technology industry is constantly changing and evolving. Automation and configuration management 
 can help you embrace that change instead of avoiding it 
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

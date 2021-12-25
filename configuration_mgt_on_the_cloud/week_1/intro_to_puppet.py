#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is Puppet?

'''
Puppet is the current industry standard for managing the configuration of computers in a fleet of machines. Part of the reason why Puppet is so popular is that it's a cross-platform
tool that's been around for a while. It's an open source project that was created in 2005, and it's gone through several different versions

The latest available version at the time this Google course went live is Puppet 6, which came out in late 2018. We typically deploy puppet using a client-server architecture. 
The client is known as the Puppet agent, and the service is known as the Puppet master. When using this model, the agent connects to the master and sends a bunch of facts that 
describe the computer to the master. The master then processes this information, generates the list of rules that need to be applied on the device, and sends this list back to 
the agent. The agent is then in charge of making any necessary changes on the computer. 

Puppet is a cross-platform application available for all Linux distributions, Windows, and Mac OS. This means that you can use the same puppet rules for managing a range of different
computers. What are these rules that we keep talking about? Let's check out a very simple example. This block is saying that the package 'sudo' should be present on every computer
where the rule gets applied. If this rule is applied on 100 computers, it would automatically install the package in all of them. This is a small and simple block but can already
give us a basic impression of how rules are written in puppet.
'''

class sudo {
   package { 'sudo':
            ensure => present
           }
}


'''
Puppet will determine the type of operating system being used and select the right tool to perform the package installation. On Linux distributions, there are several package 
management systems like APT, Yum, and DNF. Puppet will also determine which package manager should be used to install the package. On Mac OS, there's a few different available 
providers depending on where the package is coming from. The Apple Provider is used for packages that are part of the OS, while the MacPorts provider is used for packages that come
from the MacPorts Project. For Windows, we'll need to add an extra attribute to our rule, stating where the installer file is located on the local desk or a network mounted resource.

uppet will then execute the installer and make sure that it finishes successfully. If you use Chocolatey to manage your windows packages, you can add an extra Chocolatey provider to
Puppet to support that. We'll add a link to more information about this in our next reading. Using rules like this one, we can get puppet to do a lot more than just install packages
for us. We can add, remove, or modify configuration files stored in the system, or change registry entries on Windows. We can also enable, disable, start, or stop the services 
that run on our computer. We can configure crone jobs, the scheduled tasks, add, remove, or modify Users and Groups or even execute external commands, if that's what we need
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Puppet Resources

# The most basic unit in Puppet is a resource, such as user, group, file, service or package.
# In other words, each resource specifies one configuration that we're trying to manage, like a service, a package, or a file. 

# Let's look at another example. In this case, we're defining a file resource

class sysctl {
   # make sure the directory exists, some distros dont have it
   file { '/etc/sysctl.d':
         ensure => directory,
        }
}

# In this case, it's a very simple rule that ensures that etc/sysctl.d exists and is a directory. Let's talk a little bit about syntax. In both our last example and this one we 
# could see that when declaring a resource in puppet, we write them in a block that starts with the resource type ,in this case File. The configuration of the resource is then 
# written inside a block of curly braces. Right after the opening curly brace, we have the title of the resource, followed by a colon. After the colon come the attributes that 
# we want to set for the resource. In this example, we're once again setting the insurer attribute with directory as the value, but we could set other attributes too

# Let's check out a different file resource
claas timezone { 
      
   file { '/etc/timezone':
         ensure => file,
         content => "UTC/n"
         replace => true,
}
   
# In this example, we're using a file resource to configure the contents of etc/timezone, a file, that's used in some Linux distributions to determine the time zone of the 
# computer. This resource has three attributes. First, we explicitly say that this will be a file instead of a directory or a symlink then we set the contents of the file 
# to the UTC time zone. Finally, we set the replace attribute to true, which means that the contents of the file will be replaced even if the file already exists. 
# We've now seen a couple examples of what we can do with the file resource. There are a lot more attributes that we could set, like file permissions the file owner, or the filemodification time. 

# How do these rules turn into changes in our computers? When we declare a resource in our puppet rules. We're defining the desired state of that resource in the system. 
# The puppet agent then turns the desired state into reality using providers.
# The provider used will depend on the resource defined and the environment where the agent is running. Puppet will normally detect this automatically without us having to do 
# anything special. When the puppet agent processes a resource, it first decides which provider it needs to use, then passes along the attributes that we configured in the 
# resource to that provider. The code of each provider is in charge of making our computer reflect the state requested in the resource
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Puppet Classes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

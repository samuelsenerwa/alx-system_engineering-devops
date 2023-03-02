<h1>  Networking basics #0 </h1>

## Resources

- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
- [LAN Network](https://en.wikipedia.org/wiki/Local_area_network)
- [WAN Network](https://en.wikipedia.org/wiki/Wide_area_network)
- [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
- [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
- [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping/ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)

## Tasks

<ul>
<li><b>0. OSI MODEL</b> <br>
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

![OSI](https://user-images.githubusercontent.com/66512735/222376484-27385464-d0b9-4808-9f32-c1508139ee4c.png)
<br>
In this project we will mainly focus on:

 - The Transport layer and especially TCP/UDP
 - The Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.<br>
</li>
<br>
<li> <b>1. Types of network</b>
<br>
LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

![networks](https://user-images.githubusercontent.com/66512735/222379090-ab522e56-994e-4d5f-8448-b388da7da970.jpg)

</li>
<br>
<li><b>2. MAC and IP address</b>
<br>
A Media Access Control (MAC) address is a string of characters that identifies a device on a network. It’s tied to a key connection device in your computer called the network interface card, or NIC. The NIC is essentially a computer circuit card that makes it possible for your computer to connect to a network. A NIC turns data into an electrical signal that can be transmitted over the network.
<br>

![mac](https://user-images.githubusercontent.com/66512735/222379999-d9d1f94b-0ba7-4237-b121-a083aabcb057.jpg)

<br>

</li>

<li><b>3. UDP and TCP</b>
<br>

![udp and tcp](https://user-images.githubusercontent.com/66512735/222381140-4962e753-1086-4218-a7d9-97be7a61272b.jpg)

</li>
<br>

<li><b>4. TCP and UDP ports</b>
<br>
Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.

If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.

While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:

  - 22 for SSH
  - 80 for HTTP
  - 443 for HTTPS
Note that a specific IP + port = socket.

Write a Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs
<br>
<li><b>5. Is the host on the network mandatory</b>

<br>
  
![giphy](https://user-images.githubusercontent.com/66512735/222382779-8ddb67e1-48ff-499f-a297-aaed25d16de5.gif)

<br>
The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

  - Accepts a string as an argument
  - Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
  - Ping the IP 5 times
  
</li>
</ul>

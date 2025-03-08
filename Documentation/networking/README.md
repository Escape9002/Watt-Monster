To add routes after a reboot on a "normal" Debian system, append the following lines to your ```/etc/network/interfaces```-file underneath the interface you want to add the routes to ( to find the interface, run the command once in the terminal and print the routing table)  
I am looking for a dynamic solution because I am currently not sure if my interfaces might change name. You might want to change that.  

finally here are the lines:  
```
post-up ip route add x.x.x.x/mask via gateway
``` 

----

some general commands:  
- ``` ip route add x.x.x.x/mask via gateway ``` 
manually add route, this will be lost after a reboot
- ``` ip route ```
show routing tabel at the moment
- ```systemctl restart networking```
restart the networking only, not the full server

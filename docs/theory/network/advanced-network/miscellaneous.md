# Miscellaneous

TODO - reorganize these things

* iperf3
  * set up server: `iperf3 -s -p [port_number]` 
  * connect to a server `iperf3 -c [ip] -p [port_number] -t [time]` 
    * ref: [https://support.cumulusnetworks.com/hc/en-us/articles/216509388-Throughput-Testing-and-Troubleshooting](https://support.cumulusnetworks.com/hc/en-us/articles/216509388-Throughput-Testing-and-Troubleshooting)
  * 客户端使用 udp 连接服务器：加 `-u` 参数（在服务端使用该参数无效）
    * ref：[https://iperf.fr/iperf-doc.php](https://iperf.fr/iperf-doc.php)
  * How to interpret the throughput values in the result?
    * ref: [https://unix.stackexchange.com/questions/257143/how-do-i-interpret-iperf3-results](https://unix.stackexchange.com/questions/257143/how-do-i-interpret-iperf3-results)
  * 传输时收端收到的数据显著少于发端发出的数据：可能是因为其测试原理导致最后一段发出的数据未被接收
    * ref: [https://github.com/esnet/iperf/issues/382](https://github.com/esnet/iperf/issues/382)
* mininet
  * walkthrough & cheatsheet
    * [https://github.com/mininet/mininet/wiki/Introduction-to-Mininet\#what](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet#what)
    * [http://mininet.org/walkthrough/](http://mininet.org/walkthrough/)
    * show nodes, ports, port numbers and net topology: [https://stackoverflow.com/questions/30989366/how-to-figure-out-port-information-in-mininet](https://stackoverflow.com/questions/30989366/how-to-figure-out-port-information-in-mininet)
  * trace a packet with wireshark
    * `mininet> h1 wireshark &` 
    * ref: [https://github.com/mininet/mininet/issues/341](https://github.com/mininet/mininet/issues/341)
* Floodlight
  * ERROR: Got a FlowRemove message for a infinite timeout flow
  * 解决：很可能是因为创建了属性重复的 flow，有旧的 flow 被踢了，注意检查创建过程
  * ref：[https://github.com/floodlight/floodlight/issues/529](https://github.com/floodlight/floodlight/issues/529)


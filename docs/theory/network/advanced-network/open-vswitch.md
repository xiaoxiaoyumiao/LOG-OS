# Open vSwitch



* OpenFlow spec
  * [https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.3.1.pdf](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.3.1.pdf)
* ovs-vsctl, ovs-ofctl, ovs-appctl

```text
试图删除所有queue时提示仍有reference
解决：先清空QoS table
sudo ovs-vsctl -- --all destroy QoS
sudo ovs-vsctl -- --all destroy Queue

试图为新建的br0添加eth0提示出错
解决：需要设置为内部类型
ovs-vsctl add-port br0 port0 -- set Interface port0 type=internal 
ref: https://github.com/openvswitch/ovs-issues/issues/110

add switch:
sudo ovs-vsctl add-br br0

add internal port to switch:
sudo ovs-vsctl add-port br0 port0 -- set Interface port0 type=internal
ref: 
https://github.com/openvswitch/ovs-issues/issues/110
http://www.openvswitch.org/support/dist-docs/ovs-vsctl.8.txt

add flow template:
sudo ovs-ofctl add-flow S3 "priority=10,in_port=3,dl_type=0x0800,nw_src=10.0.0.3,nw_dst=10.0.0.6,actions=set_queue:123,output:1" --protocol=OpenFlow13

show flow template:
sudo ovs-ofctl dump-flows S2 --protocol=OpenFlow13

flow 具有 match 和 action 两个属性。
ovs action:
ref: 
http://www.openvswitch.org/support/dist-docs/ovs-actions.7.txt
https://man7.org/linux/man-pages/man7/ovs-actions.7.html


ref: 
https://www.openvswitch.org/support/dist-docs-2.5/tutorial/Tutorial.md.html
http://www.openvswitch.org/support/dist-docs/ovs-ofctl.8.txt
```

* cheatsheet
  * [https://randomsecurity.dev/posts/openvswitch-cheat-sheet/](https://randomsecurity.dev/posts/openvswitch-cheat-sheet/)
  * [https://gist.github.com/djoreilly/c5ea44663c133b246dd9d42b921f7646](https://gist.github.com/djoreilly/c5ea44663c133b246dd9d42b921f7646)
  * [https://docs.pica8.com/pages/viewpage.action?pageId=3083175\#:~:text=ovs%2Dofctl%20add%2Dflow%20dl\_vlan%3D%3C,ranges%20from%200%20to%204095.](https://docs.pica8.com/pages/viewpage.action?pageId=3083175#:~:text=ovs%2Dofctl%20add%2Dflow%20dl_vlan%3D%3C,ranges%20from%200%20to%204095.)
* version negotiation failed
  * 使用 --protocol 参数
  * ref: [https://bugzilla.redhat.com/show\_bug.cgi?id=1278136](https://bugzilla.redhat.com/show_bug.cgi?id=1278136)
* queue: [https://docs.pica8.com/display/picos292cg/Configuring+QoS+Queue](https://docs.pica8.com/display/picos292cg/Configuring+QoS+Queue)


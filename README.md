# Implementing and improving HDFS in DistAlgo
<https://sites.google.com/a/stonybrook.edu/sbcs535/projects/hdfs-distalgo>

There are 5 distalgo nodes in the software.
Start these nodes in order using the following commands in 5 terminals:
1) start_cluster: python3 -m da -n snode  start_cluster.da
2) namenode:  python3 -m da -n nnode -D  NameNode.da
3) datanodes: python3 -m da -n dnode -D DataNode.da
4) client:  python3 -m da -n cnode -D Client.da
5) user: python3 -m da -n unode -D User.da


User.da contains all operations user wants to perform.
start_cluster starts NameNode, DataNodes and Users.
If more users need to be started concurrently, change this in start_cluster.da

To run any test case, copy the User.da and start_cluster.da from the test case folder into src.
Then run the 5 commands listed above to run the test case.

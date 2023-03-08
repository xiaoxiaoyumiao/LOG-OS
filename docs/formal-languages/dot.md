DOT is a markdown language for constructing graphs. Use GraphViz to generate graphs from a DOT script.

Edotor is a handy online DOT editor where you can see the generated graph instantly.

```
digraph finite_state_machine {
  rankdir=TB;
  
  node1 [ label = "label1" ]
  node2 [ label = "label2" ]
  // ...
  node1 -> node2 [ label = "edge label" ]

  subgraph g1 {
    node3 -> node4 -> node5
    node3 -> node5
  }
}
```

There is no way to guarantee that edges do not cross; however you can organize the order of nodes to some extent with subgraphs.

```
// This is an anonymous subgraph
{ rank = same; edge [style=invis]; A -> B -> C }
```

## References

[1] https://graphviz.org/about/
[2] https://www.graphviz.org/doc/info/lang.html
[3] https://edotor.net/
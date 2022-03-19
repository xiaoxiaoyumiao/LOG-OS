# Framework

## Static Structure

ProtoBuf 之间的引用关系：

```text
GraphDef
|- repeated NodeDef
   |- string name
   |- string op
   |- repeated string input
   |- string device
   |- map<string, AttrValue> attr
      |- AttrValue
      |- oneof value
         |- DataType type
         |- bytes s
         |- int64 i
         |- float f
         |- bool b
         |- TensorShapeProto shape
            |- repeated Dim dim
               |- int64 size
               |- string name
            |- bool unknown_rank # if num of dims is unknown
         |- TensorProto tensor
            |- DataType dtype
            |- TensorShapeProto tensor_shape
            |- bytes tensor_content
            |- repeated <dtype> <val_name> # flattened tensor in row major order
         |- NameAttrList func
            |- string name
            |- map<string, AttrValue> attr
         |- ListValue list # a list of something
            |- repeated <one_of_types_above> <val_name>
         |- string placeholder
```


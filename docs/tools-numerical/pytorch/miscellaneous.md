# Miscellaneous

* Torchvision 0.6.0 doesn't work on Ubuntu 16.04.3 with Python 3.5.2
  * [https://github.com/pytorch/vision/issues/2132](https://github.com/pytorch/vision/issues/2132)
* module.to\(\)
  * move to a specific device
* print\(module\) 可以把一个模型的组成按照树的结构打印出来。 

- hook
  - use `register_hook` to register a callback function on a tensor or module for its forward / backward prop event. This can help debug gradient calculation issue.
  - ref: https://pytorch.org/docs/stable/generated/torch.Tensor.register_hook.html
  - ref: https://blog.paperspace.com/pytorch-hooks-gradient-clipping-debugging/

# Linker Options

* CODE
  * CODE 可以接收如下参数形式：
    * 若干个地址范围，表示可重定位的 CODE 段可被分配的地址区间，也就是代码可以被放在哪些区间内。
    * 若干个 section 的名称（section 名称参见 M51 相关），用来界定列出的 section 的先后顺序。section 还可以附带一个地址信息，表示希望将这个 section 定位在何处。
    * 用例：
    * ```text
      # CODE relocated in 0-0x3FFF and 0x8000-0xFFFF
      BL51 MYPROG.OBJ CODE(0 - 0x3FFF, 0x8000 - 0xFFFF)

      # FUNC1, FUNC2 at beginning of CODE
      BL51 A.OBJ CODE(?PR?FUNC1?A, ?PR?FUNC2?A)

      # FUNC1 at 0x800H; FUNC2 after FUNC1
      BL51 A.OBJ CODE(?PR?FUNC1?A (0x800), ?PR?FUNC2?A)
      ```


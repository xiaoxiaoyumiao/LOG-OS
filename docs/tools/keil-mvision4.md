# Keil μvision4

Keil搭建C8051F开发环境：从零开始的配置步骤

1. 安装Keil μvision4
2. 安装SiC8051F\_uVision.exe
3. 建立新项目，Device应选择Silicon Laboratories Inc.下的C8051Fxxx（相应型号）。
4. 添加需要的源文件。
5. 连接USB适配器。
6. 进入Target options，设置如下：
   1. Target中Xtal配置晶振频率，主要用于仿真
   2. Output中勾选Create HEX File，Format为HEX-80
   3. Debug中勾选右侧Use: Silicon Labs C8051Fxxx Driver，右侧Settings中勾选USB Debug Adapter，下方应当能自动检测适配器型号
   4. Utilities中Use target driver for flash programming下拉菜单选择Silicon Labs C8051Fxxx Driver，右侧Settings中全部勾选
7. 项目配置完成，build，download，等待更新驱动程序、擦除、写入。
8. 上方放大镜+红色d图标Start/stop debug session进入/推出调试，Run按钮即可在片上开始运行程序，Halt停止，Reset复位

安装silicon驱动插件driver, options for project - debug - use Silicon ... driver , settings - USB utility - use ... for flash programming: Silicon ... driver 于是download的按钮进入可用状态，可读写


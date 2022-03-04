# mobiToEPUB
This project is intend to convert mobi comic to epub for iPad, and depends on kindleunpack and kindle comic converter.
这个项目用于个人将mobi格式的漫画转化为epub格式方便iPad阅读

此项目依赖于
* Python2&3.5+
* kcc
* kindleunpack及其依赖项

使用方法
* 安装kcc-master下的requirement、python3.5+、python2(需要将python.exe改名为python2.exe并添加到PATH)
* 在mobiToEPUB.py中配置基础目录，并运行一次进行初始化
* 将mobi漫画放入基础目录\mobi\下，执行mobiToEPUB.py脚本

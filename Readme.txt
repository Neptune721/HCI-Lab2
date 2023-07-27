Windows环境：
1.Install Python(Anaconda)
2.打开 Anaconda Prompt
3.
切换盘符：D:
切换目录：cd 目录名称
4.
激活conda：conda activate
创建python3.7虚拟环境：conda create -n speech python=3.7
激活虚拟环境： conda activate speech 
5.
pip配置清华镜像源：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 
6.
安装SpeechRecognition：pip install SpeechRecognition
7.
下载二进制包：https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx
8.
将whl文件放在项目目录下
9.
安装二进制包：pip install pocketsphinx-0.1.15-cp37-cp37m-win_amd64.whl 
10.
安装PyAudio：pip install PyAudio
11.
安装PyQT5：pip install PyQT5
12.
运行程序：python asr.py
pip3 install 指定阿里云仓库
    pip3 install --index-url https://mirrors.aliyun.com/pypi/simple/ <package-name>

windows 安装 rasa
	使用anaconda创建虚拟python环境,关闭代理
	python版本  3.7.16
	pip3 install -U pip
	pip3 install rasa

安装完后创建目录
使用命令：
	https://rasa.com/docs/rasa/command-line-interface
rasa init 初始化模型
rasa train 训练模型
    rasa train --domain .\domain.yml --endpoints .\endpoints.yml
	模型保留在你init时指定路径下的models目录
	
rasa shell  
	-m 指定模型路径
	加载训练好的模型
    rasa shell -m .\models\20240623-182724-crabby-jackdaw.tar.gz  --endpoints .\endpoints.yml
	
如何自定义对话内容：
	修改：data/nlu.yml
		  data/stories.yml
		  domain.yml里面的intent
	然后执行rasa train
	https://zhuanlan.zhihu.com/p/702625825

报错：
    from rasa_sdk import Action, Tracker
    ModuleNotFoundError: No module named 'rasa_sdk'
	pip3 install rasa_sdk
	E:\桌面管理\AI模型个人\project\rasa\Scripts>pip3.exe install rasa_sdk
	
如何执行自定义action:
	https://www.cnblogs.com/huangqihui/p/10986406.html

跑action
	rasa run actions
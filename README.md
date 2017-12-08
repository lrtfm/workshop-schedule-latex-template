# 小型讨论会 \LaTeX 模板
下载地址: https://github.com/lrtfm/workshop-schedule-latex-template
## 依赖
- TeXLive
- Python 2.7

## 文件
1. 原始文件
	- `schedule.tex` : 主 \TeX 文件.
	- `reports.json` : 讨论会报告人及报告信息.
	- `table.json` : 讨论会表格信息.
	- `json2tex.py` : 用于使用信息文件 `table.json` 和 `reports.json` 生成 `table.tex` 和 `reports.tex`.
	- `make-pdf.bat` : 批处理文件, 用于生成最终 `PDF`.
2. 生成文件
	- `table.tex` : \TeX 表格.
	- `reports.json` : 会议报告及报告人详细信息.



## 如何使用
1. 修改主文件 `schedule.tex`, 填写会议题目等信息. 
	- `titlepage` 环境内相关信息
	- `会议信息` 章节相关内容
2. 在文件 `reports.json` 中填写报告信息. 单个报告信息结构如下:
	``` json
	{
		"id": "0001",
		"name": "张三",
		"school": "某大学",
		"enname": "San ZHANG",
		"enschool": "X University",
		"profile":"某大学教授",
		"title": "偏微分方程求解",
		"abstract": "介绍求解偏微分方程的主流数值方法"       
	}
	```
	`profile` 字段为报告人简介.
3. 根据时间安排填写 table.json`.
4. 生成 `pdf` 的有如下两种可选方式:
	1) 直接运行 `make-pdf.bat`
	2) 先运行 `json2tex.py` 生成必要的 `tex` 文件, 然后使用 `xelatex` 编译 `schedule.tex`.

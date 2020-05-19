# 晶体管转移特性曲线自动分析
[`English`](/README.md) **`中文`**

**FETAnal** 可自动分析由[**Kathley 探针台**](http://www.tek.com/Keithley)所测定的场效应晶体管转移特性数据，给出迁移率、阈值电压、开关比等计算结果。

## 广告
[![](https://img.shields.io/badge/下载自GitHub-CLab%20for%20Windows-important?style=for-the-badge&logo=github)](https://github.com/Z-H-Sun/NICSA/releases/download/v1.081/CLab_Win_Release.NICSA_1.081%2BFETAnal_1.041.zip)|[![](https://img.shields.io/badge/下载自百度云-提取码：csme-informational?style=for-the-badge&logo=google-cloud)](https://pan.baidu.com/s/1QjKGhEvYMKCmh4mWc1mJIg)
---|---
* 最新发布 `CLab`，点击上方按钮下载！**它是 Windows 平台上的[`NICSA`](https://github.com/Z-H-Sun/NICSA)与`FETAnal`两个模块的合集，其大小与单个模块相当，但可同时实现两者功能。**

## 特性
* 跨平台的Python程序，用户友好
* 批量自动处理，鲁棒性好
* 自带曲线平滑操作，排除离群值干扰
* 提供详尽的信息（包括迁移率随栅压变化的关系 *μ*(*V*<sub>gs</sub>)）

## 更新日志

### 1.041 版
<p align="center"><img src="/update1.png" width="90%" height="90%"></p>

* 请注意自该版本起，配置文件从`Config.ini`更名为`FETAnal.config`，并提供更多功能
* 优化用户界面（仅对 Windows 用户）
* 现可双击`CreateDesktopShortcuts.exe`以自动创建带预设的桌面快捷方式，方便调用（仅对 Windows 用户）
* 目前该程序由[`Nuitka`](https://github.com/Nuitka/Nuitka)编译，由于其能将Python代码转为C语言编译，运行速度比CPython解释器还快一倍！（仅对 Windows 用户）
* 启用更好的 GUI 后台（Windows 版从 Tk/Tcl 改为 Qt，Mac 版从 MacOSX 改为 Tk/Tcl 或 Qt）
* 实验性功能：
  * 可自定义窗口大小
  * 调整了控制台窗口（仅限 Windows）和 GUI 窗口的默认位置，保证它们不会重叠到一起
  * 将 GUI 窗口标题设置为输入文件名

### 1.04 版
* 切换至`xlrd`来读取电子文档，不再依赖 MS Excel OLE，处理速度更快
* 新增 \*nix 系统（Mac / Linux）支持
* 解决文件名中含空格的问题
* 当前设置将显示在终端中以供检查
* 自动获取电压、电流所在列 `ColGateV`、`ColIDrain`
* 修复程序错误

## 运行环境 及 下载地址

### Windows [![](https://img.shields.io/badge/Windows版下载-FETAnal%20Ver%201.041-0078d6?style=plastic&logo=windows)](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Win_Release.zip)
* Windows 7 **64位** 或以上版本
* **推荐** 使用编译版本，因其运行速度更快。下载此[发行包](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Win_Release.zip)，解压至任意路径并运行`FETAnal\FETAnal.exe`

  * 需要安装 Microsoft Visual C++ Redistributable for Visual Studio 2015-2019 ([![](https://img.shields.io/badge/下载-VC运行时库-00599c?style=plastic&logo=c%2B%2B)](https://aka.ms/vs/16/release/vc_redist.x64.exe))，否则系统将提示“vcruntime140.dll缺失”。不过，**很有可能你之前已经安装过了**，因为不少软件都依赖此运行库
* **【广告】或者，你可以下载`CLab`，其中包括了`FETAnal`，但功能更强大！** [![](https://img.shields.io/badge/Windows版下载-CLab%20%28含%20FETAnal%29-0078d6?style=plastic&logo=windows)](https://github.com/Z-H-Sun/NICSA/releases/download/v1.081/CLab_Win_Release.NICSA_1.081%2BFETAnal_1.041.zip)
* **如果你是开发者**，希望调试程序并使用**自己的Python环境**，则可下载开发者工具包。但是，自1.041版起不再维护且**不推荐使用**，如果需调试请参考[之前版本](https://github.com/Z-H-Sun/FETAnal/tree/v1.04)

### Mac OS [![](https://img.shields.io/badge/Mac%20OS%20X版下载-FETAnal%20Ver%201.041-999999?style=plastic&logo=apple)](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Mac.zip)
* Mac OS X 10.10 或更高版本

好消息是，系统自带 Python 2.7（含 Matplotlib 1.3 和 Numpy 1.8）；坏消息是，后者没有`xlrd`库。你可以选择自行安装， **或者，可以选择下载[这个](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Mac.zip)集成有 xlrd 1.2.0 的包** （该扩展是由官网 [PyPI.org](https://pypi.org/project/xlrd/) 获得的）

### Linux [![](https://img.shields.io/badge/Linux%20克隆该库-FETAnal%20Ver%201.041-e95420?style=plastic&logo=ubuntu)](https://github.com/Z-H-Sun/FETAnal.git)
* 需有桌面环境以显示 GUI
* Python >= 2.7 含

  * Numpy >= 1.8
  * Matplotlib >= 1.3
  * xlrd >= 1.0
  
只需 [FETAnal](/FETAnal) 及配置文件 [FETAnal.config](/FETAnal.config) 。运行 `chmod +x FETAnal` 以添加“可执行”标志

### 附加说明
对于 \*nix 系统 (Mac OS X 和 Linux), 如果你配有 Python3 而非 Python2 环境, **最好将 `FETAnal` 的第一行改为 `#!/usr/bin/env python3`**

## 用法简介
* 详细用法参见英文说明文档（同时提供样例以参考）的[How to use](/README.md#how-to-use)一节
* 针对Windows用户，高于1.041版本时可双击运行`CreateDesktopShortcuts.exe`以自动创建带预设的桌面快捷方式，方便调用
* 针对Mac用户，**请确保打开方式为“实用工具-终端(Utilities-Terminal)”。如果从网上下载，系统 Gatekeeper 可能阻止程序运行，请到 系统偏好-安全与隐私-通用 中放行**
* 使用前需要按照说明，根据实验测定条件修改配置文件 [FETAnal.config](/FETAnal.config)

  * 必须按照实验条件赋值介电层属性，长宽比，电子表格中电流、电压所在列号等参数，否则程序无法给出正确结果。“[样例](#样例)”一节将给出更详细的说明
  * 如果你将`ColGateV`和`ColIDrain`设为零，则程序会自动从电子表格中找出 *V*<sub>gs</sub> 和 *I*<sub>ds</sub> 所在列号。此时，你必须严格保证列标题分别为“GateV”和“IDRAIN”/“IDLIN”
  * 如果你将`W`和`L`设为零，程序会自动从文件名中提取沟道长宽数据。此时，你在保存数据时必须按如下方式命名：\*\<width\>\*\<length\>\*.xls，其中\<width\> or \<length\>必须为整数，**且后面跟有相同的单位（如 um 表示微米）**。一些可接受的命名方式有：100um, 1mm, 50 um, 50-um, 50_um 等
  * 1.041 版的配置文件中写有一些实验性功能。虽然不太可能发生，但若造成意外，请删除那几行的代码
* 将单/多个电子表格或它们所在的整个目录拖拽至应用程序（仅限Windows），或拖入终端窗口（各平台通用）并回车，开始自动分析
  * 对于Windows编译版，可以将可执行文件创建桌面快捷方式以方便调用：这样可直接将输入文件（夹）拖至快捷方式上便可用该程序打开此输入文件
  * 注意文件名请勿超过 260 字符（受限于 Python 本身）
  * 也可在终端窗口中手动输入文件名，但请注意转义文件名中间的空格。或输入 `-config` 以打开`FETConfig.config`进行配置的检查和更改
* 数据处理流程：使用Savitzky-Golay算法对每个传输曲线进行平滑处理，然后每五个点进行一次线性拟合。这一步是为了消除仪器测定偶然波动产生的离群值的干扰。然后使用以下公式获得迁移率(*μ*)和阈值电压(*V*<sub>th</sub>)：<p align="center">√*I*<sub>ds</sub> = √\[(*μ C' W*)/(2*L*)\] (*V*<sub>gs</sub> − *V*<sub>th</sub>)</p>
* 程序将直接跳过不合法的电子表格（比如，某个文件测的不是转移特性曲线）
* 程序将在终端显示其中一些重要计算结果（正向扫描(f)和反向扫描(b)中的最大迁移率(*μ*)和阈值电压(*V*\_th)，以及开关比），如下图所示<p align="center"><img src="/screenshot.png" width="80%" height="80%"></p>
* 上述结果也会存于下列电子表格中 `./Results/Results_mmddyy_HHMMSS.csv`；更详细的数据存于另一文件 `./Results/Data_mmddyy_HHMMSS.csv`，后者包括了随栅压变化的关系 *μ*(*V*<sub>gs</sub>) 和 *V*<sub>th</sub>(*V*<sub>gs</sub>)
* 转移特性曲线图像显示于一个独立的图形用户界面窗口中（见上图），其中方块散点图作出了√*I*−*V*关系，实线为平滑后的结果，虚线为取到最大迁移率处的线性拟合，“+”散点图作出了*μ*−*V*<sub>gs</sub>关系，不同颜色区分正扫/回扫
* 这些图像也存于`./Results`文件夹中
* 滚动鼠标滚轮以查看上/下一个结果

## 样例
* [此处](/Examples)提供两个样例，你可以[点此下载为zip压缩文件](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.04/Examples.zip)
* 对于`arc CNT`, 请按此设置：DIELECTRIC = 0; W, L = 0, 0; TD\[0\] = 300，意为介电层是300 nm厚的氧化硅，且从文件名中自动提取长宽比
* 对于`cytop`，请按此设置：DIELECTRIC = -1; DCP = 3.7e-9，因为（按某特定流程制备的）CYTOP介电层的单位面积电容为 3.7×10<sup>−9</sup> F/cm<sup>2</sup>；此外，令 W, L = 20, 1，表明每一个器件沟道的长宽比均为 1/20，此时无需在文件名中包含该数据。注意该文件夹中，TPDBP-C-3-o 记录的是输出特性曲线而非转移特性曲线，但无需担心，程序将将其自动跳过
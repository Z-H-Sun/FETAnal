# FETAnal
**`English`** [`中文`](/README_zh-CN.md)

Automatic analysis of FET transfer transfer characteristics data recorded by a [**Kathley**](http://www.tek.com/Keithley) semiconductor test system. Calculated mobility, threshold voltage and on/off ratio of each test will be given.

## Advertisement
[![](https://img.shields.io/badge/Download%20at%20GitHub-CLab%20for%20Windows-important?style=for-the-badge&logo=github)](https://github.com/Z-H-Sun/NICSA/releases/download/v1.081/CLab_Win_Release.NICSA_1.081%2BFETAnal_1.041.zip)|[![](https://img.shields.io/badge/Download%20at%20BaiduPan-Passcode:%20csme-informational?style=for-the-badge&logo=google-cloud)](https://pan.baidu.com/s/1QjKGhEvYMKCmh4mWc1mJIg)
---|---

* Now a combined package of `FETAnal` and [`NICSA`](https://github.com/Z-H-Sun/NICSA) on Windows, `CLab`, is released! **It takes up about the same space as either of the modules but does both modules' job.** Click the button above to download

## Features
* A cross-platform python program
* High robustness
* User friendly
* Automatic analysis in batch mode
* Build-in smoothing function for the transfer curve
* Produces detailed information such as mobility-voltage correlation *μ*(*V*<sub>gs</sub>)

## What's new

### Version 1.041
<p align="center"><img src="/update1.png" width="90%" height="90%"></p>

* Starting from this version, please note that the configuration file was renamed from `Config.ini` to `FETAnal.config`, which bears more functions
* Optimized user interface (For Windows users)
* Users can now create a desktop shortcut with preset setups by simply double-clicking `CreateDesktopShortcuts.exe` (For Windows users)
* The executable is now compiled by [`Nuitka`](https://github.com/Nuitka/Nuitka), which translates Python into a C level program and runs **twice as fast** as the native CPython interpreter! (For Windows users)
* The release package switched to a better backend for GUI (Tk/Tcl → Qt for Windows users, MacOS → Tk/Tcl or Qt for Mac users)
* Experimental features:
  * Customizable window size
  * Automatic placement of the the console window (*for Windows only*) and the figure window so that they will not overlap
  * Changed the figure title to the name of the input file

### Version 1.04
* Switched to `xlrd`: no more dependency on Microsoft Excel OLE, and process faster
* Added support for \*nix systems (Mac/Linux)
* Solved the "space-in-filename" issue
* Current settings will be printed out in the terminal for checking
* Automatically get `ColGateV` and `ColIDrain`
* Bug fixes

## Runtime Environment and Download Links
The requirements listed below are recommended for running this program. If not met, however, workarounds are also provided here.

### For Windows [![](https://img.shields.io/badge/Download%20for%20Windows-FETAnal%20Ver%201.041-0078d6?style=plastic&logo=windows)](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Win_Release.zip)
* Windows 7 **64-bit OS** or higher
* **It is recommended** to use the compiled program, because it is now a C-level program and runs much faster. You can download the [release package](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Win_Release.zip), extract it to anywhere, and run `FETAnal\FETAnal.exe`

  * You will need Microsoft Visual C++ Redistributable for Visual Studio 2015-2019 installed ([![](https://img.shields.io/badge/Download-VCRedist-00599c?style=plastic&logo=c%2B%2B)](https://aka.ms/vs/16/release/vc_redist.x64.exe)); otherwise, the system will prompt you that "vcruntime140.dll is missing." However, **it is very likeyly that you have already installed it** because a lot of other softwares depend on it
* **\[Ad\] Alternatively, you can download `CLab`, which includes `FETAnal` but is more than `FETAnal`!** [![](https://img.shields.io/badge/Download%20for%20Windows-CLab%20%28with%20FETAnal%29-0078d6?style=plastic&logo=windows)](https://github.com/Z-H-Sun/NICSA/releases/download/v1.081/CLab_Win_Release.NICSA_1.081%2BFETAnal_1.041.zip)

* If you, **as a developer**, want to debug the source code and use **your own Python** environment, you can download the developers' package. It is no longer under maintenance since version 1.0.4. Although it is not recommended, if you would still like to do so, please refer to the documentation of [previous versions](https://github.com/Z-H-Sun/FETAnal/tree/v1.04) ~~with an executable, `FETAnal.exe`, served as "wrapper script", which enables the drag-drop function and prevents abrupt exit on error. You must make sure you have~~

  * ~~Python 2.7/3.4 or higher and with the following library~~

    * ~~Numpy >= 1.12 \[also required by Matplotlib\]~~
    * ~~Matplotlib >= 2.2~~
    * ~~xlrd >= 1.0~~
  * ~~No VC runtime library required~~

### For Mac OS [![](https://img.shields.io/badge/Download%20for%20Mac%20OS%20X-FETAnal%20Ver%201.041-999999?style=plastic&logo=apple)](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Mac.zip)
* Mac OS X 10.10 or higher

Fortunately, Python 2.7 with Matplotlib 1.3 and Numpy 1.8 was built-in to Mac OS X. However, `xlrd` should be set up additionally; **Or, if you do not want to deal with those `pip` stuff, we provide [this package](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.041/FETAnal_1.041_Mac.zip) with xlrd 1.2.0 integrated** \(which was extracted from official website [PyPI.org](https://pypi.org/project/xlrd/)\).

### For Linux [![](https://img.shields.io/badge/Git%20Clone%20for%20Linux-FETAnal%20Ver%201.041-e95420?style=plastic&logo=ubuntu)](https://github.com/Z-H-Sun/FETAnal.git)
* Must be with a desktop environment to display GUI
* Python >= 2.7 with

  * Numpy >= 1.8
  * Matplotlib >= 1.3
  * xlrd >= 1.0
  
After proper deployment, only [FETAnal](/FETAnal) and [FETAnal.config](/FETAnal.config) need to be downloaded. Place them in the same folder. Run `chmod +x FETAnal` in bash to make it executable.

For \*nix systems (Mac OS X and Linux), if you have deployed a Python3 environment rather than Python2, you may want to change the first line of `FETAnal` to `#!/usr/bin/env python3` instead.

## How to use
### Before you run
* Be sure to follow the instructions in [the previous section](/README.md#runtime-environment-and-download-links) to **download and set up properly**.
* For Windows Version 1.081, you can run `CreateDesktopShortcuts.exe` first for more convenient usage;
* Make sure you have **set up all experimental parameters properly in `FETAnal.config`** following the instructions inside, including the dielectric layer property, length-to-width ratio, column number in the spreadsheet, etc. The section [Examples](/README.md#examples) will show you more detailedly about the settings.
* If you leave `ColGateV` and `ColIDrain` zeros, the program will automatically find the column numbers of *V*<sub>gs</sub> and *I*<sub>ds</sub> from spreadsheets, in which case you must make sure that the column headers are named exactly as "GateV" and "IDRAIN"/"IDLIN", respectively.
* If you leave `W` and `L` zeros, the program will automatically find the widths and lengths of channel from filenames, in which case you must name the spreadsheet files this way: \*\<width\>\*\<length\>\*.xls, where \<width\> or \<length\> must be an interger **followed by the same unit**, "um" (some acceptable versions: 100um, 1mm, 50 um, 50-um, 50_um, etc.).
* The config file of the 1.041 version was written with some experimental functions. *If they mess things up, which are not likely, please delete those lines*.

### Run the program
* For Windows and Mac OS X, double-click on the executable to run;

  * For Mac OS X, **make sure that the default application for executables is "Utilities → Terminal"**
  * For Mac OS X, execution of Internet files may be blocked by the system's gatekeeper; **you can manually allow running this program in System Preferences → Security & Privacy → General**
* For either Windows, Mac, or Linux, you can also run `<path/to/>FETAnal` in cmd/bash to lunch the program;
* When prompted to "Enter \`-config' or .xls files array or their path", you can do any of the following:

  * Entering `-config`, which will open `FETAnal.config` for you to check or change the settings;
  * Entering a folder's name, after which all the .xls or .xlsx files inside will be analyzed;
  * Entering a single filename, or a series of filenames, **each separated with space**, after which these .xls or .xlsx files will be analyzed

    * No need to worry if any spreadsheet among them are *not* generated by transfer characteristics measurements, since they will be ignored by the program;
    * Note that if the filename/dirname contains spaces, you need to use quotation marks to wrap around it (or in Mac OS, you can use `\ ` to escape a space character)
    * The filename/dirname should not be longer than 260 characters, which is caused by Python, so please don't blame me for that :)

  * Dragging the folder/file/files of interest to the terminal, which can save effort in inputing (Typically, the system will take care of the "space-in-filename" issue for you, so you do not need to do anything else);
  * \[For Windows only\], dragging the folder/file/files *to the executable* **can do the same trick with above**;

    * For the compiled version, it would be more convenient if you **create a desktop link** (shortcut) to `FETAnal.exe`, because then you can **drag the folder/file/files directly to that shortcut and open it with `FETAnal`**

* For either Windows, Mac OS, or linux, to run `<path/to/>FETAnal [bar] [foo]` in cmd/bash **is equivalent to** running the program without arguments followed by entering `[bar] [foo]` to the program;

### Results Output
<p align="center"><img src="/screenshot.png" width="80%" height="80%"></p>

* Data processing: each transfer curve is smoothed with a Savitzky-Golay filter, and then every five points are taken for a linear fit. The mobility (*μ*) and threshold voltage (*V*<sub>th</sub>) are then extracted using the following equation:<p align="center">√*I*<sub>ds</sub> = √\[(*μ C' W*)/(2*L*)\] (*V*<sub>gs</sub> − *V*<sub>th</sub>)</p>
* For each spreadsheet, unless not applicable, the program will print some important results to the terminal as shown in the picture above. They are: maximal mobility (*μ*) and threshold voltage (*V*\_th) in both forward scan (f) and backward scan (b), and on/off ratio.
* The aforementioned results will also be saved to `./Results/Results_mmddyy_HHMMSS.csv`, which you may open with Microsoft Excel. *If multiple files are analyzed, the path of the first file will be taken as the storage path.* A more detailed and exhaustive report is saved to `./Results/Data_mmddyy_HHMMSS.csv`, including the correlation between mobility/threshold voltage and gate voltage, *μ*(*V*<sub>gs</sub>) and *V*<sub>th</sub>(*V*<sub>gs</sub>).
* Figure of transfer curves will be shown in a separate GUI window, where square (scatter gram) is for √I-V, solid line for smoothed transfer curve, dashed line for linear fit (where *μ* is maximal), "+" (scatter gram) for mobility-voltage correlation, and different colors for distinguishing a forward scan from a backward one.
* These figures are stored at "./Results/\<filename\>.png" (or .svg, .bmp or some other formats else if you change `PICEXT` in `FETAnal.config`).
* Scroll the mouse wheel on the figure to view the previous/next one.

## Examples
* Two examples are provided [here](/Examples). You can download them as a zip file [here](https://github.com/Z-H-Sun/FETAnal/releases/download/v1.04/Examples.zip).
* For 'arc CNT', set DIELECTRIC = 0, W, L = 0, 0, and TD\[0\] = 300 which means the dielectric layer is SiOx of 300 nm thick, and the length-to-width ratio will be automatically extracted from filenames.
* For 'cytop', set DIELECTRIC = -1 and DCP = 3.7e-9, since the reported capacitance of CYTOP dielectric layer (processed through a certain procedure) is 3.7×10<sup>−9</sup> F/cm<sup>2</sup>; besides, set W, L = 20, 1, which means the length-to-width ratio of the channel is 1/20 for **every test** (so you do not need to specify in the filename). Note that in this folder, 'TPDBP-C-3-o' recorded the data of output characteristics rather than transfer characteristics, but do not worry since the program will leave it alone and process the data in other files properly.

## Developers
* If you want to compile the Python script on Windows, you may use [`Nuitka`](https://github.com/Nuitka/Nuitka) by running `Compile\make.bat`. ~~It is crucial **not** to install `numpy` higher than 1.16.2 nor `matplotlib` higher than 3.0.2. *If you don't believe that, just try and you'll know why*.~~ (Already fixed by higher versions)
* This tool is rather unreliable at the current stage, and it is usually very tricky to compile executables. Please see [the corresponding section in `NICSA`](https://github.com/Z-H-Sun/NICSA#developers) for reference

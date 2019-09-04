As instructed in the README documentation, drag either of the directories to the terminal or executable, and the analysis will start in batch mode.

Before that, you may have to check the settings of the experimental parameters in Config.ini:

For 'arc CNT', set DIELECTRIC = 0, W, L = 0, 0, and TD[0] = 300 which means the dielectric layer is SiOx of 300 nm thick, and the length-to-width ratio will be automatically extracted from filenames.

For 'cytop', set DIELECTRIC = -1 and DCP = 3.7e-9, since the reported capacitance of CYTOP dielectric layer (processed through a certain procedure) is 3.7x10^-9 F/cm^2; besides, set W, L = 20, 1, which means the length-to-width ratio of the channel is 1/20 for EVERY TEST (so you do not need to specify in the filename). Note that in this folder, 'TPDBP-C-3-o' recorded the data of output characteristics rather than transfer characteristics, but do not worry since the program will leave it alone and process the data in other files properly.
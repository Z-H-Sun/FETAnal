#!/usr/bin/env python3
# encoding: UTF-8
import os
import time
import numpy
import win32com.client
from matplotlib.pyplot import *
import warnings
import atexit

# preparatory work
os.system('title FET Analyzer v1.02 by Z. Sun')
warnings.simplefilter('ignore', np.RankWarning) # turn off polyfit warnings
def pause(): # cleanse well
    global xlsApp
    try: xlsApp.Application.Quit(); del xlsApp
    except: print('\nFailed to turn off Microsoft Excel, please do it manually.')
    print()
    os.system('pause') # to pause before crushing

atexit.register(pause)
thisDir = os.path.abspath(os.path.dirname(sys.argv[0])) # where this script locates

try: f = open(os.path.join(thisDir, 'Config.ini')); exec(f.read()); f.close() # definitions
except: print('Config file missing or damaged.'); os.system('pause'); os._exit(-1)

autowl = (W == 0 or L == 0) # read W & L in filenames
if DIELECTRIC < 0:
    cp = DCP
else:
    cp = 8.854e-7*EPS[DIELECTRIC]/TD[DIELECTRIC] # [F/cm^2] Capacitance of the channel per surface area
if DIELECTRIC == 2: # For BCB, serial connection
    cp0 = 8.854e-7*EPS[0]/TD[0]
    cp = cp*cp0/(cp+cp0)

if len(sys.argv) == 1:
    print('\nEnter "-config" or .xls files or their path here (drag-drop supported): ', end='')
    os.system('python ' + sys.argv[0] + ' ' + input())
    os._exit(0)
if sys.argv[1].lower() == "-config":
    os.chdir(thisDir)
    os.system('start config.ini'); os._exit(0)

print('\nPlease check the following parameters:\nCapacitance [F/cm^2]\tW/L [μm]\tCol # of V_gs/√I_d')
print(end="\t")
print(cp, end="\t\t")
print("%d/%d\t\t%d/%d" % (W, L, ColGateV, ColIDrain))
    
xlsApp = win32com.client.DispatchEx('Excel.Application')
xlsApp.EnableEvents = False
xlsApp.DisplayAlerts = False

if os.path.isdir(sys.argv[1]): # judge whether the input is path or files array
    path = sys.argv[1]
    files = os.listdir(sys.argv[1])
else:
    path = os.path.dirname(sys.argv[1])
    files = sys.argv[1:]

try:
    os.chdir(path)
    if not os.path.exists('Results'): os.mkdir('Results')
except: print("Path not applicable."); os.system('pause'); os._exit(-1)


def savitzky_golay(y): # Smooth data with a Savitzky-Golay filter (in fact incorporated in scipy.signal)
    global half
    if WINDOWLEN % 2 != 1 or WINDOWLEN < 1:
        raise TypeError("window_size size must be a positive odd number")
    if WINDOWLEN < POLYORDER + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(POLYORDER+1)
    half = (WINDOWLEN-1) // 2
    # precompute coefficients
    b = numpy.mat([[k**i for i in order_range] for k in range(-half, half+1)])
    m = numpy.linalg.pinv(b).A[0]
    # pad the signal at the extremes with values taken from the signal itself
    firstvals = y[0] - numpy.abs(y[1:half+1][::-1] - y[0] )
    lastvals = y[-1] + numpy.abs(y[-half-1:-1][::-1] - y[-1])
    y = numpy.concatenate((firstvals, y, lastvals))
    return numpy.convolve(m[::-1], y, mode='valid')


def plot_sp():
    global pic
    fig.clear()
    ax1 = gca()
    title(('# %02d: ' % (pic+1)) + results[pic][0])
    xlabel(r'$V_{\rm{gs}}\ /\ \rm{V}$', fontsize=16)
    ylabel(r'$\sqrt{I_{\rm{ds}}}\ /\ \rm{\mu A}^{1/2}$', fontsize=16)
    ax2 = twinx()
    ax2.set_ylabel(r'$\mu\ /\ (\rm{cm^2\ V^{-1}\ s^{-1}})$', fontsize=16, alpha=0.6)
    ax2.tick_params(axis='y', colors='.6')
    ax1.grid(True, linestyle='dashed')
    
    for i in [0, 1]:
        ax1.plot(results[pic][1][i], results[pic][3][i]*1e3, label=['Forward', 'Backward'][i]) # smoothed tranfer curve
        ax1.plot(results[pic][1][i], results[pic][2][i]*1e3, color='C%d' % i, alpha=.6, marker='s', markersize=4, linewidth=0) # original transfer curve
        ax2.plot(results[pic][1][i][half:-half], results[pic][4][i][0]**2*2*L/W/cp, color='C%d' % i, alpha=.6, marker='+', linewidth=0) # plot mobility against Vgs
    
    ymax = ax1.get_ylim()[1]
    for i in [0, 1]: # result of linear fitting
        sl = 1/results[pic][5][i][0]
        intc = -results[pic][5][i][1]/results[pic][5][i][0]
        ax1.plot([intc, sl*ymax/1e3+intc], [0, ymax], linestyle='dashed', alpha=.6)
        if i == 0: ax1.set_xlim(min(min(results[pic][1][0]), intc), max(max(results[pic][1][0]), intc))
    ax1.set_ylim(0, ymax)
    ymax = ax2.get_ylim()[1]
    ax2.set_ylim(0, ymax*1.2)
    ax2.yaxis.get_major_formatter().set_powerlimits((0,1))
    ax1.legend() # loc=1

def on_scroll(event):
    global pic
    if event.button == 'up':
        pic -= 1
    elif event.button == 'down':
        pic += 1
    if pic == len(results): pic = 0
    if pic < 0: pic = len(results)-1
    fstr = results[pic][0]
    fstr = fstr+' '*(25-len(fstr)) if len(fstr) < 25 else fstr[:22]+'...'
    print(('\rPlotting data for # %02d: ' % (pic+1)) + fstr, end='')
    event.canvas.figure.clear()
    plot_sp() # plot the previous/next figure
    event.canvas.draw()
    
fl = open('Results/Results_' + time.strftime('%m%d%y_%H%M%S') + '.csv', 'w', encoding='utf-8')
fd = open('Results/Data_' + time.strftime('%m%d%y_%H%M%S') + '.csv', 'w', encoding='utf-8')
print('\nName\t\t\tμ_f [cm^2 / (V s)]\tV_thf [V]\tμ_b [cm^2 / (V s)]\tV_thb [V]\tI_On/I_Off')
fl.write('\uFEFF') # BOM
fd.write('\uFEFF') # BOM
fl.write('Entry,Name,μ_f[cm^2/(V s)],V_thf[V],μ_b[cm^2/(V s)],V_thb[V],I_On/I_Off\n')
results = []

fig = figure(figsize=(8, 5))
fig.canvas.mpl_connect('scroll_event', on_scroll)
rc('font', family='Arial', size=12)
rc('mathtext', fontset='cm')
pic = -1 # index of figure

for i in files:
    fn = os.path.splitext(os.path.basename(i))
    if fn[1]!=".xls": continue
    print('%02d'%(pic+2), end=' ')
    print(fn[0]+' '*(25-len(fn[0])) if len(fn[0]) < 25 else fn[0][:22]+'...', end='') # when the filename is too long
    fl.write(str(pic+2)+','+fn[0]+',')
    fd.write(fn[0]+',#'+str(pic+2)+'\nV_g[V],')
    if autowl:
        import re
        try: W, L = map(lambda x: int(x[:-2]), re.findall(r'\d*um', fn[0],flags=re.I))
        except: print('Bad filename.'); fl.write('\n'); fd.write('\n'); continue

    try:
        wb = xlsApp.Workbooks.Open(os.path.abspath(i))
        wb.Checkcompatibility = False
        data = numpy.array(wb.Worksheets('Data').UsedRange.Value[1:]).T
        wb.Close(SaveChanges=False)

        gatev = numpy.array(data[ColGateV-1], dtype=float)  # dtype must be designated this way to avoid error when polyfitting
        nscan = len(gatev)//2 # forward/backward
        gatev = [gatev[:nscan], numpy.flipud(gatev[nscan:])] # flipping the backward sequence is beneficial
        fd.write(','.join(numpy.array(gatev, dtype=str).flatten()))
        fd.write('\n√I_d(smoothed)[A],')
        idlin = numpy.array(data[ColIDrain-1], dtype=float) # sqrt(Ids)
        idlin = [idlin[:nscan], numpy.flipud(idlin[nscan:])]
        idsg = [0, 0] # smoothed value of sqrt(Ids)
        diff = [[], []] # consist of [slope, intercept] arrays
        maxs = [[0, 0], [0, 0]] # [slope, intercept] when abs(slope) reaches a maximum
        for j in [0, 1]:
            idsg[j] = savitzky_golay(idlin[j]) # smooth the curve
            for k in range(half, nscan-half): # linear fit using every WINDOWLEN points
                polyp = numpy.polyfit(gatev[j][k-half:k+half+1], idsg[j][k-half:k+half+1], 1)
                diff[j].append(polyp)
            diff[j] = numpy.array(diff[j]).T
            maxs[j] = diff[j][:, numpy.argmax(abs(diff[j][0]))]
            mobility = '%.2E' % (maxs[j][0]**2*2*L/W/cp)
            print(mobility, end='\t\t')
            fl.write(mobility+',')
            vth = '%.2f' % (-maxs[j][1]/maxs[j][0]) # threshold voltage
            print(vth, end='\t\t')
            fl.write(vth+',')

        fd.write(','.join(numpy.array(idsg, dtype=str).flatten()))
        fd.write('\nμ[cm^2/(V s)],')
        for k in [0, 1]:
            fd.write('N/A,'*half+','.join(numpy.array(diff[k][0]**2*2*L/W/cp, dtype=str))+',N/A'*half+',')
        for j in [0, 1]: # 0=slope, 1=intercept
            fd.write('\n%s,'%['slope', 'intercept'][j])
            for k in [0, 1]: # 0=forward, 1=backward
                fd.write('N/A,'*half+','.join(numpy.array(diff[k][j], dtype=str))+',N/A'*half+',')
        fd.write('\n\n')

        ionoff = '%.2E' % (idsg[0][-1]/idsg[0][0])**2 # Ion/Ioff
        print(ionoff) # should always scan Vgs from off to on!
        fl.write(ionoff+'\n')
    except Exception as e:
        print(repr(e))
        fl.write(repr(e)+'\n')
        fd.write(repr(e)+'\n')
        continue

    pic += 1
    results.append((fn[0], gatev, idlin, idsg, diff, maxs)) # record results
    plot_sp()
    subplots_adjust(left=.10, right=.91, top=.95, bottom=.12)
    savefig('Results/' + fn[0] + PICEXT)

xlsApp.Application.Quit(); del xlsApp
print('\nResults (.csv and ' + PICEXT + ' files) were saved at: %s.' % os.path.abspath('Results'))
fl.close()
fd.close()
print('\nPlotting data for the last file.\nPlease scroll to move to the previous/next figure.\n')
show()
os._exit(0)

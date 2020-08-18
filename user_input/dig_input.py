#psychopy digit input program with simple validation
#hunter priniski, priniski@ucla.edu

from psychopy import visual, core, event

DIM = 800
window_dim = [DIM + 400, DIM]
win = visual.Window(window_dim, allowGUI = True, monitor = 'testMonitor', units ='pix', color = "black")

tens_text = visual.TextStim(win, text="_", pos = (-15, 50), height = 32)
tens_text.autoDraw = True

ones_text = visual.TextStim(win, text="_", pos = (15, 50), height = 32)
ones_text.autoDraw = True

cents = visual.TextStim(win, text = 'cents', pos = (75, 50), height = 32)
cents.autoDraw = True

tens_border = visual.Rect(win, width = 25, height = 35, pos = (-15, 50), lineWidth = 3, lineColor = 'white', autoDraw = True)
ones_border = visual.Rect(win, width = 25, height = 35, pos = (15, 50), lineWidth = 3, lineColor = 'white', autoDraw = True)
win.flip()

while tens_text.text == '_' and ones_text.text == '_':

    _ = event.waitKeys(keyList = ['0','1','2','3','4','5','6'])
    tens_response = int(_[0])
    tens_text.text = str(tens_response)
    tens_border.lineColor = 'green'
    win.flip()

    _ = event.waitKeys(keyList = ['left', 'backspace','0','1','2','3','4','5','6','7','8','9'])

    if _[0] == 'left' or _[0] == 'backspace':
        tens_text.text = '_'
        tens_border.lineColor = 'white'
        win.flip()

    else:
        ones_response = int(_[0])
        ones_text.text = str(ones_response)
        ones_border.lineColor = 'green'
        win.flip()


core.wait(1.0)

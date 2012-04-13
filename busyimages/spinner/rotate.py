import os

inkscapecmd = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape --export-png="

stext = "<g transform=\"rotate(180,76,76)\">"

numberOfFiles = 90
step = 360 / numberOfFiles

currentAngle = step
loop = 1
for i in range(0,numberOfFiles):
    rtext = "<g transform=\"rotate("+str(currentAngle)+",76,76)\">"
    #print rtext
    
    svg = open("spinner_white.svg")
    output = open("tempsvg.svg", 'w')
    for s in svg:
        #print s.replace(stext, rtext)
        output.write(s.replace(stext, rtext))
    
    outputpng = "spinner_"+str(i)+".png"
    outputcmd = inkscapecmd + outputpng + " tempsvg.svg"
    os.system(outputcmd)
    
    currentAngle = currentAngle + step
    loop = loop + 1


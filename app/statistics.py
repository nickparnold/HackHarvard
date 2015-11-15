import os
import subprocess
import time
def energyStats(user, passw, stateInput, acSize):
    proc = subprocess.Popen(["python", "nest.py", "--user", user, "--password", passw, "curtemp"], stdout=subprocess.PIPE)
    currtem = proc.communicate()[0].strip('\n')
    proc = subprocess.Popen(["python", "nest.py", "--user", user, "--password", passw, "curtarget"], stdout=subprocess.PIPE)
    pregoaltem = proc.communicate()[0].strip('\n')
    state = stateInput.upper()
    ton = int(acSize[:-3])
    timedegrees = float(input("What is the time per degrees that was calibrated in minutes? -- pull from nest calibration:   ")) #run calibration
    allowance = float(input("What is the allowance perday? --  pull from treadline datapoint:   "))
    amps = {'1':7, '1.5':10.5, '2': 14, '2.5':17.5,'3':21, '3.5':24.5,'4':28}
    areacost = {'WA': 7.24,'OR':8.13, 'CA':14.37, 'NV':11.82,'ID':6.35,'MT':8.72,'WY':7.73 ,'UT':8.17,'AZ':9.66,'NM':9.03,'CO':9.18,'ND':7.28,'SD':8.01,'NE':7.52,'KS':8.26,'OK':8.59,'TX':12.41,'MN':9.02,'IA':9.34,'MO':7.57,'AR':8.73,'LA':9.38,'WI':10.26,'IL':10.40,'MS':9.40,'MI':10.72,'IN':8.12,'KY':7.19,'TN':7.79,'MS':9.40,'AL':9.24,'OH':9.51,'WV':6.63,'VA':8.72,'NC':9.35,'SC':9.18,'GA':9.07,'FL':11.20, 'NY':17.05,'VT':14.13,'NH':14.81, 'MA':16.33,'RI':14.02,'CT':18.67,'DE':13.17,'MD':11.77,'DC':11.17, 'HI':24.13,'AK':15.12,'NJ':14.44, 'PA':10.96}
    cost = areacost[state]
    wattage = amps[ton] * 240 #determine the watts
    kilowatth = wattage/1000 #determine the kilowatt-hour
    costph = cost * kilowatth
    timedegrees = timedegrees/60
    moneyperdegree = timedegrees * costph
    deltacurr = float(currtem) - float(pregoaltem) #difference in temperature to goal
    pregoalcost = moneyperdegree * deltacurr
    deltabudg = (deltacurr * allowance) / pregoalcost
    print(deltabudg)
    if deltacurr < 0:
      newgoaltemp = float(currtem) + float(deltabudg)
    else:
      newgoaltemp = float(currtem) - float(deltabudg)
    if abs(deltacurr) < abs(deltabudg):
      newgoaltemp = pregoaltem
    os.system("python nest.py --user "+ str(user)+" --password "+ str(passw)+" temp " + str(newgoaltemp))

def calibrate(user, password):
    proc = subprocess.Popen(["python", "nest.py", "--user", user, "--password", passw, "curtemp"], stdout=subprocess.PIPE)
    currtem = proc.communicate()[0].strip('\n')
    time_start = time.time()

    sleep(1)
    proc = subprocess.Popen(["python", "nest.py", "--user", user, "--password", passw, "curtemp"], stdout=subprocess.PIPE)
    currtem = proc.communicate()[0].strip('\n')
    duration = time.time() - time_start
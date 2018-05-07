import math
from sing import*


class conver(Singleton):
# class to convert data according to the international system Сi


    # function for conversion into a finite result number, an argument for transformation, a number reduction
    def end_nume(self,num,arg,skr):
        if num == 0:
            return 'err 0'
        elif num < 0:
            return 'err 1'
        num = float(num)
        if arg == 0:
            num = num / 10 ** 6
        elif arg == 1:
            num = num / 10 ** 3
        elif arg == 2:
            num = num
        elif arg == 3:
            num = num / 10 ** -3
        elif arg == 4:
            num = num / 10 ** -6
        elif arg == 5:
            num = num / 10 ** -9
        elif arg == 6:
            num = num / 10 ** -12
        num = round(num,skr)
        return num
    # function to convert to a total result number, an argument to convert
    def st_nume(self,num,arg):
        num = float(num)
        if arg == 0:
            return num * 10**6
        elif arg == 1:
            return num * 10 ** 3
        elif arg == 2:
            return num
        elif arg == 3:
            return num * 10 ** -3
        elif arg == 4:
            return num * 10 ** -6
        elif arg == 5:
            return num * 10 ** -9
        elif arg == 6:
            return num * 10 ** -12



class resist(Singleton):
# calculation of parallel and sequential joints

    # calculation of serial connection of the resistance and parallel capacitance
    def zac_res_ps(self,val1,val2,setr):
        val1 = float(val1)
        val2 = float(val2)
        if setr == 'R3' or setr == 'C3':
            return val1 + val2
        elif setr == 'R2' or setr == 'R1' or setr == 'C1' or setr == 'C2':
            return val2 - val1
    #calculation of serial parallel resistance and serial capacitance
    def zac_res_pr(self,val1,val2,setr):
        val1 = float(val1)
        val2 = float(val2)

        if (val1 == val2) and (setr != 'C3' and setr != 'R3'):
            return 0
        if setr == 'R3' or setr == 'C3':
            if val1 == val2:
                return val1/2
            else:
                return 1/(1/val1 + 1/val2)
        elif (setr == 'R1' or setr == 'R2' or setr == 'C1' or setr == 'C2') and val1>val2:
            return 1/((1/val2) - (1/val1))
        else:
            return 0

class sin_reac(Singleton):
# calculation in alternating current

    #reactive resistance of L element val1 and val2 arguments setting what you need to find
    def reacL(self,val1,val2,seting):
        if seting == 'XL':
            return 2*math.pi*val1*val2
        elif seting == 'L' and val2 > 0 and val1 > 0:
            return val2 / (2*math.pi*val1)
        elif seting == 'f':
            return (val2 /val1)/(2*math.pi)

    # reactive resistance of C element val1 and val2 arguments setting what you need to find
    def reacCp(self,val1,val2,seting):
        if (seting == 'XC' or seting == 'C' or seting == 'f') and (val1 > 0 and val2 > 0):
            return 1/(2*math.pi*val1*val2)

    # impedance f - frequency. c- Capacity, l - inductance, r -resistance,setting what you need to find
    def impendans(self,f,c,l,r,seting):
        if f > 0 and c > 0 and l >0 and seting == 0:
            return math.sqrt(r**2+(self.reacL(f,l,'XL')-self.reacCp(f,c,'XC'))**2)
        elif seting == 1 and r <= 0:
            return 0
        elif f > 0 and c > 0 and l >0 and seting == 1 and r > 0:
            R = 1/r**2
            xl = 1/self.reacL(f,l,'XL')
            xr = 1/self.reacCp(f,c,'XC')
            return 1/math.sqrt(R+(xl-xr)**2)

class om_zk(Singleton):
# community formulas
    # power and Ohm's law
    def zev_p(self,arg1,arg2,seting):
        if seting == 1:
            return arg1*arg2
        elif seting == 2:
            return (arg1**2)*arg2
        elif seting == 3:
            return (arg1**2)/arg2
        elif seting == 4:
            return (arg1*arg2)**0.5
        elif seting == 5:
            return arg1/arg2
        elif seting == 6:
            return (arg1/arg2)**0.5
        elif seting == 7:
            return arg1/arg2**2
    # resistance to the element
    def om_el(self,arg1,arg2,arg3):
        return (arg1-arg2)/arg3
    # Ohm's law
    def zac_om(self,arg1,arg2,seting):
        arg1 = float(arg1)
        arg2 = float(arg2)
        if seting == 'U':
            return arg1*arg2
        elif seting == 'R' or seting == 'I':
            return arg1 / arg2

from maths import *
import os

class logick:
    def __init__(self):
        self.converted = conver()
        self.conecteds = resist()
        self.sind = sin_reac()
        self.om = om_zk()
    # call calculator
    def clas(self):
        os.system('calc')
    #data checking
    def test_from(self,a):
        for i in range(len(a)):
            try:
                if float(a[i].text()) <= 0:
                    raise ValueError
            except:
                a[i].setText('')
                a[i] = 'err'
            else:
                a[i] = float(a[i].text())
        return a
    # Ohm's law
    def om_sh(self):
        tab = [self.ui.line1,self.ui.line2,self.ui.line3]
        args = self.test_from(tab)
        pos = self.ui.find.currentText()
        if pos == 'U' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1],self.ui.val2.currentIndex())
            arg2 = self.converted.st_nume(args[2],self.ui.val3.currentIndex())
            self.ui.line1.setText(str(self.converted.end_nume(self.om.zac_om(arg1, arg2, pos), self.ui.val1.currentIndex(),self.num_skr)))
        elif pos == 'R' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val1.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val3.currentIndex())
            self.ui.line2.setText(str(self.converted.end_nume(self.om.zac_om(arg1, arg2, pos), self.ui.val2.currentIndex(),self.num_skr)))
        elif pos == 'I' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val1.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val2.currentIndex())
            self.ui.line3.setText(str(self.converted.end_nume(self.om.zac_om(arg1, arg2, pos), self.ui.val3.currentIndex(),self.num_skr)))
    # resistance consistently
    def res_ps(self):
        tab = [self.ui.line_resps1, self.ui.line_resps2, self.ui.line_resps3]
        args = self.test_from(tab)
        pos = self.ui.find_resps.currentText()

        if pos == 'R1' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_resps2.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_resps3.currentIndex())
            self.ui.line_resps1.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_resps1.currentIndex(),self.num_skr)))
        elif pos == 'R2' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_resps1.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_resps3.currentIndex())
            self.ui.line_resps2.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_resps2.currentIndex(),self.num_skr)))
        elif pos == 'R3' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_resps1.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val_resps2.currentIndex())
            self.ui.line_resps3.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_resps3.currentIndex(),self.num_skr)))
    # resistance in parallel
    def res_pr(self):
        tab = [self.ui.line_respr1, self.ui.line_respr2, self.ui.line_respr3]
        args = self.test_from(tab)
        pos = self.ui.find_respr.currentText()

        if pos == 'R1' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_respr2.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_respr3.currentIndex())
            self.ui.line_respr1.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_respr1.currentIndex(), self.num_skr)))
        elif pos == 'R2' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_respr1.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_respr3.currentIndex())
            self.ui.line_respr2.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_respr2.currentIndex(), self.num_skr)))
        elif pos == 'R3' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_respr1.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val_respr2.currentIndex())
            self.ui.line_respr3.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_respr3.currentIndex(), self.num_skr)))
    # cp consistently
    def cp_ps(self):
        tab = [self.ui.line_cpps1, self.ui.line_cpps2, self.ui.line_cpps3]
        args = self.test_from(tab)
        pos = self.ui.find_cpps.currentText()

        if pos == 'C1' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_cpps2.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_cpps3.currentIndex()+2)
            self.ui.line_cpps1.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_cpps1.currentIndex()+2, self.num_skr)))
        elif pos == 'C2' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cpps1.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_cpps3.currentIndex()+2)
            self.ui.line_cpps2.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_cpps2.currentIndex()+2, self.num_skr)))
        elif pos == 'C3' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cpps1.currentIndex()+2)
            arg2 = self.converted.st_nume(args[1], self.ui.val_cpps2.currentIndex()+2)
            self.ui.line_cpps3.setText(str(self.converted.end_nume(self.conecteds.zac_res_pr(arg1, arg2,pos), self.ui.val_cpps3.currentIndex()+2, self.num_skr)))
    # cp in parallel
    def cp_pr(self):
        tab = [self.ui.line_cppr1, self.ui.line_cppr2, self.ui.line_cppr3]
        args = self.test_from(tab)
        pos = self.ui.find_cppr.currentText()

        if pos == 'C1' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_cppr2.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_cppr3.currentIndex()+2)
            self.ui.line_cppr1.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_cppr1.currentIndex()+2, self.num_skr)))
        elif pos == 'C2' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cppr1.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_cppr3.currentIndex()+2)
            self.ui.line_cppr2.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_cppr2.currentIndex()+2, self.num_skr)))
        elif pos == 'C3' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cppr1.currentIndex()+2)
            arg2 = self.converted.st_nume(args[1], self.ui.val_cppr2.currentIndex()+2)
            self.ui.line_cppr3.setText(str(self.converted.end_nume(self.conecteds.zac_res_ps(arg1, arg2,pos), self.ui.val_cppr3.currentIndex()+2, self.num_skr)))
    # reactive resistance L
    def reac_L(self):
        tab = [self.ui.line_Lf, self.ui.line_LL, self.ui.line_LXL]
        args = self.test_from(tab)
        pos = self.ui.find_XL.currentText()

        if pos == 'f' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_LL.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_Lr.currentIndex())
            self.ui.line_Lf.setText(str(
                self.converted.end_nume(self.sind.reacL(arg1, arg2, pos), self.ui.val_Lf.currentIndex(), self.num_skr)))
        elif pos == 'L' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_Lf.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_Lr.currentIndex())
            self.ui.line_LL.setText(str(
                self.converted.end_nume(self.sind.reacL(arg1, arg2, pos), self.ui.val_LL.currentIndex()+2, self.num_skr)))
        elif pos == 'XL' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_Lf.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val_LL.currentIndex()+2)
            self.ui.line_LXL.setText(str(
                self.converted.end_nume(self.sind.reacL(arg1, arg2, pos), self.ui.val_Lr.currentIndex(), self.num_skr)))
    # reactive resistance C
    def reac_Cp(self):
        tab = [self.ui.line_cpf, self.ui.line_cpc, self.ui.line_cpXC]
        args = self.test_from(tab)
        pos = self.ui.find_XC.currentText()

        if pos == 'f' and args[1] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[1], self.ui.val_cpC.currentIndex()+2)
            arg2 = self.converted.st_nume(args[2], self.ui.val_cpr.currentIndex())
            self.ui.line_cpf.setText(str(
                self.converted.end_nume(self.sind.reacCp(arg1, arg2, pos), self.ui.val_cpf.currentIndex(), self.num_skr)))
        elif pos == 'C' and args[0] != 'err' and args[2] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cpf.currentIndex())
            arg2 = self.converted.st_nume(args[2], self.ui.val_cpr.currentIndex())
            self.ui.line_cpc.setText(str(
                self.converted.end_nume(self.sind.reacCp(arg1, arg2, pos), self.ui.val_cpC.currentIndex()+2, self.num_skr)))
        elif pos == 'XC' and args[0] != 'err' and args[1] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_cpf.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val_cpC.currentIndex()+2)
            self.ui.line_cpXC.setText(str(
                self.converted.end_nume(self.sind.reacCp(arg1, arg2, pos), self.ui.val_cpr.currentIndex(), self.num_skr)))
    # impundence
    def impned(self):
        tab = [self.ui.line_Zf, self.ui.line_ZC, self.ui.line_ZL,self.ui.line_ZR]
        args = self.test_from(tab)
        pos = self.ui.pos_z.currentIndex()
        if args[0] != 'err' and args[1] != 'err' and args[2] != 'err' and args[3] != 'err':
            arg1 = self.converted.st_nume(args[0], self.ui.val_Zf.currentIndex())
            arg2 = self.converted.st_nume(args[1], self.ui.val_Zc.currentIndex()+2)
            arg3 = self.converted.st_nume(args[2], self.ui.val_Zl.currentIndex()+2)
            arg4 = self.converted.st_nume(args[3], self.ui.val_Zr.currentIndex())
            self.ui.line_Z.setText(str(
                self.converted.end_nume(self.sind.impendans(arg1, arg2, arg3, arg4, pos), self.ui.find_Z.currentIndex(), self.num_skr)))
    # converter
    def convert(self):
        cv1 = [self.ui.ch1v,self.ui.ce1v,self.ui.cl1v,self.ui.cm1v,self.ui.cv1v,self.ui.ci1v,self.ui.cvt1v]
        tab = [self.ui.ch1, self.ui.ce1, self.ui.cl1, self.ui.cm1, self.ui.cv1, self.ui.ci1, self.ui.cvt1]
        cv2 = [self.ui.ch2v,self.ui.ce2v,self.ui.cl2v,self.ui.cm2v,self.ui.cv2v,self.ui.ci2v,self.ui.cvt2v]
        line_find = [self.ui.ch2,self.ui.ce2,self.ui.cl2,self.ui.cm2,self.ui.cv2,self.ui.ci2,self.ui.cvt2]
        args = self.test_from(tab)
        for i in range(len(args)):
            if args[i] != 'err':
                if i == 1:
                    find = self.converted.end_nume(self.converted.st_nume(args[i], cv1[i].currentIndex()+2), cv2[i].currentIndex()+2,
                                          self.num_skr)
                    line_find[i].setText(str(find))
                elif i == 2:
                    find = self.converted.end_nume(self.converted.st_nume(args[i], cv1[i].currentIndex()+2), cv2[i].currentIndex()+2,
                                          self.num_skr)
                    line_find[i].setText(str(find))
                else:
                    find = self.converted.end_nume(self.converted.st_nume(args[i],cv1[i].currentIndex()),cv2[i].currentIndex(),self.num_skr)
                    line_find[i].setText(str(find))
    # Ohm's law and power
    def P_ze(self):
        tab =[self.ui.P1,self.ui.U1,self.ui.R1,self.ui.I1]
        lines = [self.ui.v11.currentIndex(),self.ui.v22.currentIndex(),self.ui.v33.currentIndex(),self.ui.v44.currentIndex()]
        args = self.test_from(tab)
        pos = self.ui.pos_z_2.currentText()
        # U and R
        if args[1] != 'err' and args[2] != 'err' and pos == 'U-R':
            f = self.om.zev_p(self.converted.st_nume(args[1], lines[1]), self.converted.st_nume(args[2], lines[2]), 3)
            f1 = self.om.zev_p(self.converted.st_nume(args[1], lines[1]), self.converted.st_nume(args[2], lines[2]), 5)
            self.ui.P1.setText(str(self.converted.end_nume(f, lines[0], self.num_skr)))
            self.ui.I1.setText(str(self.converted.end_nume(f1, lines[3], self.num_skr)))
        # R and I
        elif args[2] != 'err' and args[3] != 'err' and pos == 'R-I':
            f = self.om.zev_p(self.converted.st_nume(args[3], lines[3]), self.converted.st_nume(args[2], lines[2]), 2)
            f1 = self.om.zev_p(self.converted.st_nume(args[2], lines[2]), self.converted.st_nume(args[3], lines[3]), 1)
            self.ui.P1.setText(str(self.converted.end_nume(f, lines[0], self.num_skr)))
            self.ui.U1.setText(str(self.converted.end_nume(f1, lines[1], self.num_skr)))
        # U and I
        elif args[1] != 'err' and args[3] != 'err' and pos == 'U-I':
            f = self.om.zev_p(self.converted.st_nume(args[1], lines[1]), self.converted.st_nume(args[3], lines[3]), 1)
            f1 = self.om.zev_p(self.converted.st_nume(args[1], lines[1]), self.converted.st_nume(args[3], lines[3]), 5)
            self.ui.P1.setText(str(self.converted.end_nume(f, lines[0], self.num_skr)))
            self.ui.R1.setText(str(self.converted.end_nume(f1, lines[2], self.num_skr)))
        # P and U
        elif args[0] != 'err' and args[1] != 'err' and pos == 'P-U':
            f = self.om.zev_p(self.converted.st_nume(args[1], lines[1]), self.converted.st_nume(args[0], lines[0]), 3)
            f1 = self.om.zev_p(self.converted.st_nume(args[0], lines[0]), self.converted.st_nume(args[1], lines[1]), 5)
            self.ui.R1.setText(str(self.converted.end_nume(f, lines[2], self.num_skr)))
            self.ui.I1.setText(str(self.converted.end_nume(f1, lines[3], self.num_skr)))
        # P and R
        elif args[0] != 'err' and args[2] != 'err' and pos == 'P-R':
            f = self.om.zev_p(self.converted.st_nume(args[0], lines[0]), self.converted.st_nume(args[2], lines[2]), 4)
            f1 = self.om.zev_p(self.converted.st_nume(args[0], lines[0]), self.converted.st_nume(args[2], lines[2]), 6)
            self.ui.U1.setText(str(self.converted.end_nume(f, lines[1], self.num_skr)))
            self.ui.I1.setText(str(self.converted.end_nume(f1, lines[3], self.num_skr)))
        # P and I
        elif args[0] != 'err' and args[3] != 'err' and pos == 'P-I':
            f = self.om.zev_p(self.converted.st_nume(args[0], lines[0]), self.converted.st_nume(args[3], lines[3]), 5)
            f1 = self.om.zev_p(self.converted.st_nume(args[0], lines[0]), self.converted.st_nume(args[3], lines[3]), 7)
            self.ui.U1.setText(str(self.converted.end_nume(f, lines[0], self.num_skr)))
            self.ui.R1.setText(str(self.converted.end_nume(f1, lines[2], self.num_skr)))
    # resistance elements
    def R_lem(self):
        tab = [self.ui.ug, self.ui.ue, self.ui.ie]
        lines = [self.ui.ugf.currentIndex(),self.ui.uef.currentIndex(),self.ui.ief.currentIndex(),self.ui.ref.currentIndex()]
        args = self.test_from(tab)
        if args[0] != 'err' and args[1] != 'err' and args[2] != 'err':
            f = self.om.om_el(self.converted.st_nume(args[0],lines[0]),self.converted.st_nume(args[1],lines[1]),self.converted.st_nume(args[2],lines[2]))
            self.ui.re.setText(str(self.converted.end_nume(f, lines[3], self.num_skr)))



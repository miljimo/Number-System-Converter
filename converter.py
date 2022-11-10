"""
  @changes:
   1. move to python 3 on 10/11/2022
"""

from tkinter import (
    Frame,
    StringVar,
    LabelFrame,
    Label,
    Radiobutton,
    Entry,
    END,
    Tk,
    NW,
    RIGHT,
)

import re

BITS = 8


class FrmCal(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parentWindow = parent
        self.initForm()

    def initForm(self):

        self.parentWindow.title("Number system converter")
        self.choicePanel(self.parentWindow, 0, 0, title="Input Options")

        self.inputPanel(self.parentWindow, 0, 1)
        self.resultPanel(self.parentWindow, 0, 3, "Results")

       
        self.StringStatus = StringVar()
        self.StringStatus.set("Ready...")
        self.lblStatus = Label(self.parentWindow, textvariable=self.StringStatus)
        self.lblStatus.config(
            font="Arial 10 italic",
        )
        self.lblStatus.grid(column=0, row=4, padx=4, pady=4, sticky=NW)
        self.grid()
        self.center()
        self.parentWindow.resizable(0, 0)
        self.parentWindow.mainloop()

    
    def choicePanel(self, parentWindow, x, y, title=""):
        self.frameOptionals = LabelFrame(parentWindow, text=title, width=40)
        self.frameOptionals.config(font="Arial 14 normal ")
        self.frameOptionals.grid(column=x, padx=4, pady=4, row=y, sticky=NW)

       
        self.searchOptionVar = StringVar()
        self.btnDec = Radiobutton(
            self.frameOptionals,
            command=self.ModeChanger,
            value="dec",
            text=" - Decimal",
            variable=self.searchOptionVar,
            underline=3,
        )
        self.btnDec.grid(column=0, row=0, padx=4, pady=4, sticky=NW)
        self.btnDec.select()
       
        self.optionBin = Radiobutton(
            self.frameOptionals,
            command=self.ModeChanger,
            value="bin",
            text=" - Binary",
            variable=self.searchOptionVar,
            underline=3,
        )
        self.optionBin.grid(column=1, row=0, padx=4, pady=4, sticky=NW)
        self.optionBin.deselect()
       
        self.optionOct = Radiobutton(
            self.frameOptionals,
            command=self.ModeChanger,
            value="oct",
            text=" - Octal",
            variable=self.searchOptionVar,
            underline=3,
        )
        self.optionOct.grid(column=2, row=0, padx=4, pady=4, sticky=NW)
        self.optionOct.deselect()
       
        self.optionHexDeci = Radiobutton(
            self.frameOptionals,
            command=self.ModeChanger,
            value="hex",
            text=" - Hex-Decimal",
            variable=self.searchOptionVar,
            underline=3,
        )
        self.optionHexDeci.grid(column=3, row=0, padx=4, pady=4, sticky=NW)
       
        FrameMode = LabelFrame(self.frameOptionals, text=" MODE ")
        FrameMode.grid(column=4, row=0, padx=2, pady=2, sticky=NW)
        self.lblGlobalVariableMode = StringVar()
        self.lblGlobalVariableMode.set("Decimal")
        self.labelMode = Label(
            FrameMode, text="Decimal", fg="red", textvariable=self.lblGlobalVariableMode
        )
        self.labelMode.pack()
       
   
    def inputPanel(self, parent, x, y):
        panel = Frame(parent, bg="#FFFFFF")

        panel.grid(column=x, row=y, sticky=NW, padx=0, pady=4)
        self.txtStringChar = StringVar()

        self.txtOptionEntry = Entry(
            panel, width=35, textvariable=self.txtStringChar, justify=RIGHT
        )
        self.txtOptionEntry.grid(
            column=0, row=0, sticky=NW, padx=4, pady=4, ipady=3, ipadx=7
        )
        self.txtOptionEntry.config(
            font=" Arial 17 normal",
            bd=0,
            fg="#6513F7",
            selectforeground="white",
            selectborderwidth=0,
        )

        self.txtOptionEntry.bind("<KeyRelease>", self.txtKeyRelease)

    def resultPanel(self, parent, x, y, title=""):
        resultPanelWin = LabelFrame(parent, text=title, width=40)
        resultPanelWin.grid(column=x, row=y, padx=4, pady=4, sticky=NW)
        resultPanelWin.config(width=44)

        lblBinary = Label(resultPanelWin, text="Binary")
        lblBinary.configure(font="Arial 13 normal")
        lblBinary.grid(column=0, row=1, padx=4, pady=4, sticky=NW)
        self.txtStringBinary = StringVar()
        txtBinary = Entry(resultPanelWin, textvariable=self.txtStringBinary)
        txtBinary.configure(font="Arial 13 normal", width=30, bg="#eeeeee")
        txtBinary.grid(column=1, row=1, padx=4, pady=4, sticky=NW)

        lblDecimal = Label(resultPanelWin, text="Decimal")
        lblDecimal.configure(font="Arial 13 normal")
        lblDecimal.grid(column=0, row=2, padx=4, pady=4, sticky=NW)

        self.strDecimal = StringVar()
        self.strDecimal.set("")
        txtDecimal = Entry(resultPanelWin, textvariable=self.strDecimal)
        txtDecimal.configure(font="Arial 13 normal", width=30, bg="#eeeeee")
        txtDecimal.grid(column=1, row=2, padx=4, pady=4, sticky=NW)

        lblOct = Label(resultPanelWin, text="Octal")
        lblOct.configure(font="Arial 13 normal")
        lblOct.grid(column=0, row=3, padx=4, pady=4, sticky=NW)
        self.strOctal = StringVar()
        txtOct = Entry(resultPanelWin, textvariable=self.strOctal)
        txtOct.configure(font="Arial 13 normal", width=30, bg="#eeeeee")
        txtOct.grid(column=1, row=3, padx=4, pady=4, sticky=NW)

        lblHexDeci = Label(resultPanelWin, text="Hex-Decimal")
        lblHexDeci.configure(font="Arial 13 normal")
        lblHexDeci.grid(column=0, row=4, padx=4, pady=4, sticky=NW)
        self.strHexDecimal = StringVar()
        txtHexDecimal = Entry(resultPanelWin, textvariable=self.strHexDecimal)
        txtHexDecimal.configure(font="Arial 13 normal", width=30, bg="#eeeeee")
        txtHexDecimal.grid(column=1, row=4, padx=4, pady=4, sticky=NW)

    def ModeChanger(self):
        self.emptyResult()
        self.txtStringChar.set("")
        if self.searchOptionVar.get() == "dec":
            self.lblGlobalVariableMode.set("Decimal")
        elif self.searchOptionVar.get() == "bin":
            self.lblGlobalVariableMode.set("Binary")
        elif self.searchOptionVar.get() == "oct":
            self.lblGlobalVariableMode.set("Octal")
        elif self.searchOptionVar.get() == "hex":
            self.lblGlobalVariableMode.set("Hex-decimal")
        else:
            self.lblGlobalVariableMode.set("-")

        return 0

    def setPosition(self, xpos, ypos):
        xpos = str(xpos)
        ypos = str(ypos)

        self.parentWindow.geometry("480x350+" + xpos + "+" + ypos)

    def center(self):
        self.ws = self.parentWindow.winfo_screenwidth()
        self.hs = self.parentWindow.winfo_screenheight()
       
        x = (self.ws / 2) - (450 / 2)
        y = (self.hs / 2) - (450 / 2)
        self.setPosition(x, y)

    def emptyResult(self):

        self.txtStringBinary.set("")
        self.strDecimal.set("")
        self.strHexDecimal.set("")
        self.strOctal.set("")

    def txtKeyRelease(self, event):
        self.okay()
        if self.lblGlobalVariableMode.get() == "Decimal":
            patternExpr = "^[0-9]+$"
            if re.search(patternExpr, self.txtOptionEntry.get()):
                self.emptyResult()
               
                number = int(self.txtOptionEntry.get())
               
                self.strDecimal.set(self.txtOptionEntry.get())
                self.txtStringBinary.set(self.decimalToAnyBase(number, 2))
                self.strOctal.set(self.decimalToAnyBase(number, 8))
                self.strHexDecimal.set(self.decimalToAnyBase(number, 16))

            else:
                self.removeunwantedcharacter()

        elif self.lblGlobalVariableMode.get() == "Binary":
           
            patternExpr = "^[01]+$"
            if re.search(patternExpr, self.txtOptionEntry.get()):
                self.emptyResult()
                BinaryNumber = str(self.txtOptionEntry.get()).strip()
                self.txtStringBinary.set(BinaryNumber)
                dec = self.toDecimal(BinaryNumber, 2)
                self.strHexDecimal.set(self.decimalToAnyBase(dec, 16))
                self.strDecimal.set(dec)
                self.strOctal.set(self.decimalToAnyBase(dec, 8))
            else:
                self.removeunwantedcharacter()

        elif self.lblGlobalVariableMode.get() == "Octal":

            patternExpr = "^[0-7]+$"
            if re.search(patternExpr, self.txtOptionEntry.get()):
                self.emptyResult()
                octNumber = self.txtOptionEntry.get().strip()
                self.strOctal.set(octNumber)
                toDecimal = self.toDecimal(octNumber, 8)
                self.strDecimal.set(toDecimal)
                self.txtStringBinary.set(self.decimalToAnyBase(toDecimal, 2))
                self.strHexDecimal.set(self.decimalToAnyBase(toDecimal, 16))
            else:
                self.removeunwantedcharacter()

        elif self.lblGlobalVariableMode.get() == "Hex-decimal":
            patternExpr = "^[0-9A-Fa-f]+$"
        if re.search(patternExpr, self.txtOptionEntry.get()):
            self.emptyResult()
            HexDecimalNumber = str(self.txtOptionEntry.get()).upper().strip()
            decimalNumber = self.toDecimal(HexDecimalNumber, 16)
            self.strDecimal.set(decimalNumber)
            self.txtStringBinary.set(self.decimalToAnyBase(decimalNumber, 2))
            self.strHexDecimal.set(self.decimalToAnyBase(decimalNumber, 16))
            self.strOctal.set(self.decimalToAnyBase(decimalNumber, 8))
        else:
            self.removeunwantedcharacter()
   
    def okay(self):
        self.lblStatus.config(fg="#0703F1")
        self.StringStatus.set(
            "Current Mode : "
            + self.lblGlobalVariableMode.get()
            + "\n Reading to use ..."
        )

    def removeunwantedcharacter(self):
        try:
            getStringValue = self.txtStringChar.get()
            leng = len(self.txtOptionEntry.get())
            self.txtOptionEntry.delete(leng - 1, END)
            self.lblStatus.config(fg="#F21234")
            self.StringStatus.set(
                "Error(201): This charcter ("
                + getStringValue[len(getStringValue) - 1]
                + ") is invalid in this mode..."
            )
        except:
            self.okay()
            return ""

    def Pow(self, value, power):
        power = int(power)
        multiply = 1
        while power >= 1:
            multiply *= int(value)
            power -= 1
        return multiply
       

    def toDecimal(self, strdecValue, Nobase=2):
        try:
           
            decStr = str(strdecValue)
            ItemsNo = len(decStr)
            BitPlaceValue = int(ItemsNo - 1)
            sumAccumulator = 0
            
            for bit in decStr:
                bit = str(bit).upper()
                if bit == "F":
                    swapBitStr = 15
                elif bit == "E":
                    swapBitStr = 14
                elif bit == "D":
                    swapBitStr = 13
                elif bit == "C":
                    swapBitStr = 12
                elif bit == "B":
                    swapBitStr = 11
                elif bit == "A":
                    swapBitStr = 10
                else:
                    swapBitStr = bit
               
                sumIndividual = int(swapBitStr) * self.Pow(Nobase, BitPlaceValue)
                sumAccumulator += sumIndividual
                BitPlaceValue -= 1
            return sumAccumulator
        except:
            return ""

    """
    This is function reserve the string value input has parameter
    """

    def strReverse(self, strValue):
        result = ""
        n = 0
        start = 0
        
        while strValue[n:] != "":
            while strValue[n:] != "" and strValue[n] != " ":
                n += 1 
                result = strValue[start:n] + "" + result
                start = n
        return result  

  
    def decimalToAnyBase(self, strBinValue, base=2):
        try:
            decimal = int(strBinValue)
            listBits = {}
            binValueStr = ""
            if decimal == 0:
                return 0
            else:

                while decimal != 0:

                    divValue = decimal % base
                    decimal = int(decimal / base)

                    if divValue == 15:
                        StrBaseValue = "F"
                    elif divValue == 14:
                        StrBaseValue = "E"
                    elif divValue == 13:
                        StrBaseValue = "D"
                    elif divValue == 12:
                        StrBaseValue = "C"
                    elif divValue == 11:
                        StrBaseValue = "B"
                    elif divValue == 10:
                        StrBaseValue = "A"
                    else:
                        StrBaseValue = divValue

                    listBits[len(listBits)] = StrBaseValue

               
                for item in listBits:
                    binValueStr = binValueStr + str(listBits[item])
                return self.strReverse(binValueStr)
               
        except:
            return "E####"


if __name__ == "__main__":
    root = Tk()
    calForm = FrmCal(root)

from Tkinter import *
import tkMessageBox
import re;

#const declaration
BITS=8;

"""
This class FrmCal create the Gui and the control to operate the binary convert
This utitily program is create mostly for assembling write who find it difficult to memories memory address
in hex-decimal or oct or binary

"""
class FrmCal(Frame):
    #the class constructor with just one parameter,
    #the self is a default in any method created within a class in python
    def __init__(self,parent):
        Frame.__init__(self,parent);#initial the Frame constructor method to
        #accept the parent window has it defaukt window
        self.parentWindow=parent;#create a private self.parentWindow  variable hold  the parent window
        #calling the init function to initialise the form
        self.initForm();#calling the initForm method to create the window form. 
    def initForm(self):
         #The function create the window Gui 
         self.parentWindow.title("Number system converter");#setting the window title  text
         #call the function to create the choice panel Gui
         self.choicePanel(self.parentWindow,0,0,title="Input Options")
         #calling the function to create the input Text panel
         
         self.inputPanel(self.parentWindow,0,1);
         # Calling the function to create the Result Panel
         self.resultPanel(self.parentWindow,0,3,"Results");

         #create the status label
         self.StringStatus=StringVar();
         self.StringStatus.set("Ready...");
         self.lblStatus=Label(self.parentWindow,textvariable=self.StringStatus);
         self.lblStatus.config(font="Arial 10 italic",);
         self.lblStatus.grid(column=0,row=4,padx=4,pady=4,sticky=NW);
         #position the frame on the parent window
         self.grid();
         #call the function to centralised the window 
         self.center();
         #set the window resizable to false;
         self.parentWindow.resizable(0,0);
         #call the parent window mainloop function to show the window
         #without this there will be no window on the surface of the screen
         self.parentWindow.mainloop();

               
     #this  method create the window choice panel    
    def choicePanel(self,parentWindow,x,y,title=""):
         self.frameOptionals=LabelFrame(parentWindow,text=title,width=40);
         self.frameOptionals.config(font="Arial 14 normal ");
         self.frameOptionals.grid(column=x,padx=4,pady=4,row=y,sticky=NW);

         #create the share variable
         self.searchOptionVar=StringVar();

         #add the options button to the frame
         self.btnDec=Radiobutton(self.frameOptionals,command=self.ModeChanger,value="dec",text=" - Decimal",variable=self.searchOptionVar,underline=3);
         self.btnDec.grid(column=0,row=0,padx=4,pady=4,sticky=NW);
         self.btnDec.select();


         #add the options button to the frame
         self.optionBin=Radiobutton(self.frameOptionals,command=self.ModeChanger,value="bin",text=" - Binary",variable=self.searchOptionVar,underline=3);
         self.optionBin.grid(column=1,row=0,padx=4,pady=4,sticky=NW);
         self.optionBin.deselect();

         #add the options button to the frame
         self.optionOct=Radiobutton(self.frameOptionals,command=self.ModeChanger,value="oct",text=" - Octal",variable=self.searchOptionVar,underline=3);
         self.optionOct.grid(column=2,row=0,padx=4,pady=4,sticky=NW);
         self.optionOct.deselect();

         #add the options button to the frame
         self.optionHexDeci=Radiobutton(self.frameOptionals,command=self.ModeChanger,value="hex",text=" - Hex-Decimal",variable=self.searchOptionVar,underline=3);
         self.optionHexDeci.grid(column=3,row=0,padx=4,pady=4,sticky=NW);

         #this section of the code create the current mode  frame and its properties
         FrameMode=LabelFrame(self.frameOptionals,text=" MODE ");
         FrameMode.grid(column=4,row=0,padx=2,pady=2,sticky=NW);
         self.lblGlobalVariableMode=StringVar();
         self.lblGlobalVariableMode.set("Decimal");
         self.labelMode=Label(FrameMode,text="Decimal",fg="red",textvariable=self.lblGlobalVariableMode);
         self.labelMode.pack();
         #end it here
    # this section of code create the window input panel
    def inputPanel(self,parent,x,y):
        panel=Frame(parent,bg="#FFFFFF");
       
        panel.grid(column=x,row=y,sticky=NW,padx=0,pady=4);
        self.txtStringChar=StringVar();
        
        self.txtOptionEntry=Entry(panel,width=35,textvariable=self.txtStringChar,justify=RIGHT);
        self.txtOptionEntry.grid(column=0,row=0,sticky=NW,padx=4,pady=4,ipady=3,ipadx=7);
        self.txtOptionEntry.config(font=" Arial 17 normal",bd=0,fg="#6513F7",selectforeground="white",selectborderwidth=0);


        self.txtOptionEntry.bind("<KeyRelease>",self.txtKeyRelease);
    def resultPanel(self,parent,x,y,title=""):
       resultPanelWin=LabelFrame(parent,text=title,width=40);
       resultPanelWin.grid(column=x,row=y,padx=4,pady=4,sticky=NW);
       resultPanelWin.config(width=44);

       lblBinary=Label(resultPanelWin,text="Binary");
       lblBinary.configure(font="Arial 13 normal");
       lblBinary.grid(column=0,row=1,padx=4,pady=4,sticky=NW);
       self.txtStringBinary=StringVar();
       txtBinary=Entry(resultPanelWin,textvariable=self.txtStringBinary);
       txtBinary.configure(font="Arial 13 normal",width=30,bg='#eeeeee');
       txtBinary.grid(column=1,row=1,padx=4,pady=4,sticky=NW);


       lblDecimal=Label(resultPanelWin,text="Decimal");
       lblDecimal.configure(font="Arial 13 normal");
       lblDecimal.grid(column=0,row=2,padx=4,pady=4,sticky=NW);
       
       self.strDecimal=StringVar();
       self.strDecimal.set("");
       txtDecimal=Entry(resultPanelWin,textvariable=self.strDecimal);
       txtDecimal.configure(font="Arial 13 normal",width=30,bg='#eeeeee');
       txtDecimal.grid(column=1,row=2,padx=4,pady=4,sticky=NW);


       lblOct=Label(resultPanelWin,text="Octal");
       lblOct.configure(font="Arial 13 normal");
       lblOct.grid(column=0,row=3,padx=4,pady=4,sticky=NW);
       self.strOctal=StringVar();
       txtOct=Entry(resultPanelWin,textvariable=self.strOctal);
       txtOct.configure(font="Arial 13 normal",width=30,bg='#eeeeee');
       txtOct.grid(column=1,row=3,padx=4,pady=4,sticky=NW);


       lblHexDeci=Label(resultPanelWin,text="Hex-Decimal");
       lblHexDeci.configure(font="Arial 13 normal");
       lblHexDeci.grid(column=0,row=4,padx=4,pady=4,sticky=NW);
       self.strHexDecimal=StringVar();
       txtHexDecimal=Entry(resultPanelWin,textvariable=self.strHexDecimal);
       txtHexDecimal.configure(font="Arial 13 normal",width=30,bg='#eeeeee');
       txtHexDecimal.grid(column=1,row=4,padx=4,pady=4,sticky=NW);


    def ModeChanger(self):
         self.emptyResult();
         self.txtStringChar.set("");
         if(self.searchOptionVar.get()=="dec"):
               self.lblGlobalVariableMode.set("Decimal");               
         elif(self.searchOptionVar.get()=="bin"):
               self.lblGlobalVariableMode.set("Binary");
         elif(self.searchOptionVar.get()=="oct"):
               self.lblGlobalVariableMode.set("Octal");
         elif(self.searchOptionVar.get()=="hex"):
               self.lblGlobalVariableMode.set("Hex-decimal");
         else:
               self.lblGlobalVariableMode.set("-");            
            
         return 0;

    def setPosition(self,xpos,ypos):               
        xpos=str(xpos);
        ypos=str(ypos);
        
        self.parentWindow.geometry('480x350+'+xpos+'+'+ypos);
    def center(self):
            self.ws= self.parentWindow.winfo_screenwidth()
            self.hs = self.parentWindow.winfo_screenheight()         
            
            # calculate position x, y
            x = (self.ws/2) - (450/2)
            y = (self.hs/2) - (450/2)
            self.setPosition(x,y)

    def emptyResult(self):
        
            self.txtStringBinary.set("");
            self.strDecimal.set("");
            self.strHexDecimal.set("");
            self.strOctal.set("");
  
    def txtKeyRelease(self,event):
        self.okay();#set the status label to ready
        if(self.lblGlobalVariableMode.get()=="Decimal"):
            #test if the key press is a decimal number
            patternExpr="^[0-9]+$";
            if(re.search(patternExpr,self.txtOptionEntry.get())):
                self.emptyResult();         
                                
                #calulate the hexdecimal equivalent and put the result into the hex-decimal box
                number=int(self.txtOptionEntry.get());
               
                
                #set the value of the decimal number to the txtbox of the decimal 
                self.strDecimal.set(self.txtOptionEntry.get());
                self.txtStringBinary.set(self.decimalToAnyBase(number,2));
                self.strOctal.set(self.decimalToAnyBase(number,8));
                self.strHexDecimal.set(self.decimalToAnyBase(number,16));
                
                
            else:
                    #call the function to remove the unwanted entry
                self.removeunwantedcharacter();
                
               
                
         
        elif(self.lblGlobalVariableMode.get()=="Binary"):
           #test if the key press is a decimal number
            patternExpr="^[01]+$";
            if(re.search(patternExpr,self.txtOptionEntry.get())):
                self.emptyResult();
                BinaryNumber=str(self.txtOptionEntry.get()).strip();
                self.txtStringBinary.set(BinaryNumber);
                dec=self.toDecimal(BinaryNumber,2);
                self.strHexDecimal.set(self.decimalToAnyBase(dec,16));
                self.strDecimal.set(dec);
                #convert to octal
                self.strOctal.set(self.decimalToAnyBase(dec,8));
            else:
                self.removeunwantedcharacter();
                
            

            
        elif(self.lblGlobalVariableMode.get()=="Octal"):
               
               patternExpr="^[0-7]+$";
               if(re.search(patternExpr,self.txtOptionEntry.get())):
                    self.emptyResult();
                    octNumber=self.txtOptionEntry.get().strip();
                    self.strOctal.set(octNumber)
                    #convert the base eight to decimal value
                    toDecimal=self.toDecimal(octNumber,8);
                    #set the decimal to the decimal  text box
                    self.strDecimal.set(toDecimal);
                    #now convert the decimal value to base 2 which is binary
                    self.txtStringBinary.set(self.decimalToAnyBase(toDecimal,2));
                                       
                    #convert from decimal value to  hexdecimal                    
                    self.strHexDecimal.set(self.decimalToAnyBase(toDecimal,16));
               else:
                   self.removeunwantedcharacter();
                    
                    
              
        elif(self.lblGlobalVariableMode.get()=="Hex-decimal"):
            #test if the key press is a decimal number
             patternExpr="^[0-9A-Fa-f]+$";
            if(re.search(patternExpr,self.txtOptionEntry.get())):
                self.emptyResult();
                #get the hex-decimal number 
                HexDecimalNumber=str(self.txtOptionEntry.get()).upper().strip();
                #convert it to decimal number
                decimalNumber=self.toDecimal(HexDecimalNumber,16);
                #set the decimal number to the textbox of the decimal
                self.strDecimal.set(decimalNumber);
                #convert the decimal to binary
                self.txtStringBinary.set(self.decimalToAnyBase(decimalNumber,2));
                #convert the decimal to base 16 to see if the convertion work
                self.strHexDecimal.set(self.decimalToAnyBase(decimalNumber,16));
                #convert the decimal to base 8
                self.strOctal.set(self.decimalToAnyBase(decimalNumber,8))                
            else:
                self.removeunwantedcharacter();
             

    """
     The modal function creation start here
    """
    def okay(self):
        self.lblStatus.config(fg="#0703F1");
        self.StringStatus.set("Current Mode : "+self.lblGlobalVariableMode.get()+"\n Reading to use ...");                             
                        
    def removeunwantedcharacter(self):
        try:
            getStringValue=self.txtStringChar.get();
            leng=len(self.txtOptionEntry.get());
            self.txtOptionEntry.delete(leng-1,END);
            self.lblStatus.config(fg="#F21234");
            self.StringStatus.set("Error(201): This charcter ("+getStringValue[len(getStringValue)-1]+") is invalid in this mode...");
        except:
            self.okay();
            return "";

    def Pow(self,value,power):
        #convert power parameter to integer
        power=int(power);
        #initialised the multiply variable to 1
        multiply=1;
        #while power is great than or equal to 1 loop the block of the code 
        while power >=1:
            #multiply the value in the multiply variable by the value parameter value
            multiply *= int(value);
            #decrease power by 1
            power -=1;
        return multiply ;#return the total value of the multiply
        

    def toDecimal(self,strdecValue,Nobase=2):
        try:
            #convert the string value to string again in in case it is decimal 
            decStr=str(strdecValue);
            #get the len of the string decStr; variable
            ItemsNo=len(decStr);
            #get the higest place value of binary number
            BitPlaceValue=int(ItemsNo-1);
            #create a variable call sumAccumulator and initialised to zero
            sumAccumulator=0;
            # for statement to loop inside the decStr  values
            for bit in decStr:
                #get the each bit value of the item in decStr
                bit=str(bit).upper();
                
                if(bit=="F"):
                    swapBitStr=15;
                elif(bit=="E"):
                    swapBitStr=14;
                elif(bit=="D"):
                    swapBitStr=13;
                elif(bit=="C"):
                    swapBitStr=12;
                elif(bit=="B"):
                    swapBitStr=11;
                elif(bit=="A"):
                    swapBitStr=10;
                else:
                    swapBitStr=bit;
                    
                
                    

                
                #calculating the decimal value of each place value       
                sumIndividual=int(swapBitStr) * self.Pow(Nobase,BitPlaceValue);
                #sum the sum of the place value inside the variable sumAccumulator
                sumAccumulator +=sumIndividual;
                #decrease the BitPlaceValue variable by 1
                BitPlaceValue -=1;

            #return the sumAccumulator    
            return sumAccumulator;
        except:
            return "";
    """
    This is function reserve the string value input has parameter
    """
    def strReverse(self,strValue):
        result = ""
        n = 0
        start = 0#starting point for the reverse
        #loop the string to reverse it
        while ( strValue[n:] != "" ):
            while ( strValue[n:] != "" and strValue[n] != ' ' ):
                n += 1# increment n by one
                result = strValue[ start: n ] + "" + result 
                start = n;#initialised the start point to  current n value;
        return result#return the reverse string has the return value of the function




    """
    This decimal to any base converter function with just two parameter
    first parent is the decimal number which you want to convert and the second is the base to which
    you want to convert to, by default it is to base 2 binary system
    
    """
    def decimalToAnyBase(self,strBinValue,base=2):
        try:
            #convert the value enter to integer value
            decimal=int(strBinValue);
            #create an empty dictionary object to hold the bits 
            listBits={};
            binValueStr="";
            if(decimal ==0):
                return 0;
            else:
                
                while (decimal != 0):
                       
                        divValue=decimal % base;
                        decimal= int(decimal / base)
                       
                        if(divValue ==15):
                            StrBaseValue="F";
                        elif(divValue==14):
                            StrBaseValue="E";
                        elif(divValue==13):
                            StrBaseValue="D";
                        elif(divValue==12):
                            StrBaseValue="C";
                        elif(divValue==11):
                            StrBaseValue="B";
                        elif(divValue==10):
                            StrBaseValue="A";
                        else:
                            StrBaseValue=divValue;
                                       
                        listBits[len(listBits)]= StrBaseValue;
                
                        
                #convert to string value        
                for item in listBits:
                      binValueStr = binValueStr +  str(listBits[item]);  
                
                return self.strReverse(binValueStr);#return the base converted
        except:
            return "E####";

         
if __name__ == "__main__":
        #run the application
        root=Tk();# create the main window and pass it has argument to the FrmCal constructor
        calForm=FrmCal(root);

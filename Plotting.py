import pandas as pd #use for manipulation and analysis od Data
import numpy as np # array
import matplotlib.pyplot as plt # library use for plotting and bar formation
import seaborn as sns
import sys # used for giving optional output i.e ,press 1 or 2 etc
datafile = pd.read_csv("bonds.csv") # read the output file named bonds.csv
print(datafile.head()) #just wanna print the head of my file to confirm that either my file readed successfully or not
print("\n")
print("  Welcome to Plotting script ")
print("  Here you can plot and your desired plot will be save to your directory")
print("\n")
def amino_acid(): 
    head1=np.array(datafile['LIG']) 
    head2=np.array(datafile['Amino_acid']) 
    bar(head1, head2) 

def intrections():
    column1=np.array(datafile['Amino_acid'])  
    column2=np.array(datafile['Molecule']) 
    bar_plot(column1, column2) 

def bar(head1,head2):
    new=np.arange(len(head1))
    sns.barplot(new,list(head2),palette = 'hls',saturation = 10, label='Amino acid')   

    plt.xlabel('Ligand')
    plt.ylabel('amino acid')
    plt.title('amino acid')
    plt.legend(fontsize=10)
    plt.savefig("Amino_acid.png")
    plt.show() 

def bar_plot(column1,column2):
    new=np.arange(len(column1))
    sns.barplot(new,list(column2),palette = 'hls',saturation = 10, label='Intrections')   

    plt.ylabel('No of intrections')
    plt.xlabel('Amino acid')
    plt.title('Bar Plot')
    plt.legend(fontsize=10)
    plt.savefig("Intrections.png")
    plt.show() 
while True:
    choice=int(input("To plot number of Amino acids press 1\nTo plot number of Interctions press 2\nTo exit press 0\n"))
    if choice==1:
        amino_acid()
    elif choice==2:
        intrections()
    elif choice==0:
        sys.exit(0)



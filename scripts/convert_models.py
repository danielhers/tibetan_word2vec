from subprocess import call
import os

CONVERT_BIN = 'convertvec/convertvec'
DATA_PATH = 'data/output'

def convert_bin2txt(bin_path):
    out_path = bin_path.replace('output','output_txt').replace('.bin','.txt')
    
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
        
    cmd = CONVERT_BIN + ' bin2txt ' + bin_path + ' ' + out_path
    retval = call(cmd.split())
    if retval != 0:
        print('An error has occurred.')
    else:
        print('Success.')

if __name__=='__main__':
    for root,_,files in os.walk(DATA_PATH):
        for fname in files:
            if '.bin' in fname:
                convert_bin2txt(os.path.join(root,fname))

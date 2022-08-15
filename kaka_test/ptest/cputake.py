import os
import codecs
import re

cputop_comm = "top | head -n 3|tail -n 1|cut -d , -f 4|awk -F id '{print $1}'"

ansi_regex = r'\x1b(' \
             r'(\[\??\d+[hl])|' \
             r'([=<>a-kzNM78])|' \
             r'([\(\)][a-b0-2])|' \
             r'(\[\d{0,2}[ma-dgkjqi])|' \
             r'(\[\d+;\d+[hfy]?)|' \
             r'(\[;?[hf])|' \
             r'(#[3-68])|' \
             r'([01356]n)|' \
             r'(O[mlnp-z]?)|' \
             r'(/Z)|' \
             r'(\d+)|' \
             r'(\[\?\d;\d0c)|' \
             r'(\d;\dR))'




cputop_data = os.popen(cputop_comm)
print("cputop_data-->",cputop_data)
cputop_readlines = cputop_data.readlines()
print("cputop_readlines-->",cputop_readlines)


cputop_str = str(cputop_readlines)
print("cputop_str-->",cputop_str)
cputop_utf = cputop_readlines[0].encode('utf-8')
print("cputop_utf-->",cputop_utf)


cputop_re = re.sub(ansi_regex,'',cputop_readlines[0])
print("cputop_re-->",cputop_re)

cutstr = cputop_re.split("\x1b(Bm")
print("cutstr-->",cutstr)
flocut = float(cutstr[1])
print("flocut-->",flocut)
use = 100-flocut
print("use-->",round(use,1))

'''
strt = "'\x1b(B\x1b[m\x1b[39;49m\x1b[1m100.0 \x1b(B\x1b[m\x1b[39;49m\n')"
restr = re.sub(ansi_regex,'',strt)

print("restr--->",restr)

cutstr = restr.split("\x1b(Bm")

print(cutstr[1])
use = 100-float(cutstr[1])
print(use)
#strtest = "%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st"

#strcut = ","
#strtest = "1,2,3"

#aftercut = strtest.split(strcut)

#testche = aftercut[3][-8:-3]
#st = "100.0 id"
#stcut = st[0:5]
#stuse = (100.0 - float(stcut))
#print(stuse)

#print(testche)

#print(strtest.index(","))


#print(stcut)

#print(strtest)
#print(aftercut)

'''

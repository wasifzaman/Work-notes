'''
Python Scripts for CTS
'''



#psexec copy generator script
#CN - host names
#formatted_CN - string formatted by appending CN strings
formatted_CN = ''
CN = ["LCCS-WILDE-01","LCCS-WILDE-02","LCCS-WILDE-03","LCCS-WILDE-04","LCCS-WILDE-05"]
for i in CN:
	formatted_CN += i + ','
print('psexec \\\\' + formatted_CN[:-1] + ' -u lacima\\administrator -p r7,Gk8?Yi0 cmd /c copy \\\\lcs2k8-dc01\\cts$\\sc.msi c:\\')

'''
12/11 Unfinished
"NEWTON"
'''
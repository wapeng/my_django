# encoding: utf-8
# from django.http import HttpResponse
from django.shortcuts import render
import commands
from django.views.generic import detail
import json
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World !'
    context['msg'] = json.dumps(getLinuxMsg())
    #
#     return HttpResponse("Hello world ! ")
    #给上下文返回字典
    print "============" + context['msg']
    return render(request, 'hello.html', context)


def getLinuxMsg():
    returnMsg = []
    linuxMsg = commands.getoutput(' top -bn 1 ')
    mess = linuxMsg.split('\n')
    
    for strr in mess:
        if strr.find('Cpu') >= 0:
            cpus = strr
    
    cpus = cpus[cpus.index(':') + 1:].replace('  ','').split(',')
    
    for ms in cpus:
        detail = ms.split()
        if cmp(detail[1],'us') == 0:
            returnMsg.append({'value':detail[0], 'name':'用户占用'})
        elif cmp(detail[1],'sy') == 0:
            returnMsg.append({'value':detail[0], 'name':'系统占用'})
        elif cmp(detail[1],'id') == 0:
            returnMsg.append({'value':detail[0], 'name':'空闲'})
    return returnMsg

if __name__ == '__main__':
    returnMsg = ''
    linuxMsg = commands.getoutput(' top -n 1 ')
    print 'linuxMsg' + linuxMsg
    mess = linuxMsg.split('\n')
    for strr in mess:
        print "strr" + strr
        if strr.index('Cpu') > 0:
            cpus = strr
    
    cpus = cpus[cpus.index(':') + 1:].replace('  ','').split(',')
    
    for ms in cpus:
        detail = ms.split()
        if cmp(detail[1],'us') == 0:
            returnMsg += '用户进程占用：'+ detail[0] + '%\n'
        elif cmp(detail[1],'sy') == 0:
            returnMsg += '系统进程占用：'+ detail[0] + '%\n'
        elif cmp(detail[1],'id') == 0:
            returnMsg += '空闲：'+ detail[0] + '%\n'
    print returnMsg

    
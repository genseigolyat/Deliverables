def word2dict(msg):
    temp = ''
    temp_msg = ''
    temp_list=[]
    i = 1

    for temp in msg:
        if(temp==' ' or temp=='. '):
            temp_list.append((i, temp_msg))
            temp_msg = ''
            i = i + 1
        else:
            temp_msg+=temp
    temp_list.append((i,temp_msg))
    return  temp_list

if __name__=="__main__":
    msg = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    dic = {}
    temp_list = []
    temp_list = word2dict(msg)
    for key,item in temp_list:
        if(key==1 or key == 5 or key == 6 or key == 7or key == 8or key == 9or key == 15or key == 16or key == 19):
            dic[key]=item[:1]
        else:
            dic[key]=item[:2]
    print(dic)

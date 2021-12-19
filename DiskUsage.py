import os

print('----------------------')
def DU(path=os.getcwd(),sum=0):
    sum+=os.path.getsize(path)#size of directory without considering files in it
    print(f'path:{path}  , size:{os.path.getsize(path)}')
    if len(os.listdir(path))==0:
        return sum
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path,dir)):
            sum+=DU(os.path.join(path,dir))
        else:
            sum+=os.path.getsize(os.path.join(path,dir))
            print(f'path:{os.path.join(path,dir)}  , size:{os.path.getsize(os.path.join(path,dir))}')
    return sum



    
print(DU())

print('------------------')



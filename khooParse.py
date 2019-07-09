def Parse(self,filename):
    #take filename as input via string
    fname = filename
    mfile = open(fname, "r+")
    content = mfile.read()
    print(content)
    mfile.close()
    return
    
    
#if __name__ =="__main__":
Parse("CausalCues.txt")
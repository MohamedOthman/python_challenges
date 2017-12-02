def merge_the_tools(string, k):
    chunk=[]
    counter=0
    for i in string:
        counter += 1
        if i not in chunk:
            chunk.append(i)
        if counter == k :
            print ''.join(chunk)
            counter=0
            chunk=[]

if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)

#!/usr/bin/python3
'''
Einfuhrung in die Programmierung 1.2b
'''

workArray = [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3,7,11]]
filterArray = [[1, 1, 0], [0, 2, 0], [0, 0, 3]]

def applyFilter(workArray, filterArray):
    filter_range=int((len(filterArray)-1)/2)+1
    resa = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # verschiabt des filterarry auf da y-achse
    for y in range(len(workArray[0])):
        ye = y + filter_range
        ys = y - int(filter_range/2)
        yo = 666

        if(len(workArray[0]) < ye):
            yo = filter_range

        if(y < (filter_range/2)):
            ys = 0

        # verschiabt des filterarry auf da x-achse
        for x in range(len(workArray)):
            fa = filterArray
            xe = x + filter_range
            xs = x - int(filter_range/2)
        
            if(len(workArray) - y < (filter_range/2)):
                fa = fa[-filter_range:]

            if(x < (filter_range/2)):
                xs = 0
                fa = fa[-filter_range:]

            for f in range(len(workArray[xs:xe])):
                res = 0
                # print(workArray[xs:xe][f][ys:ye])
                # print("mal")
                # print(fa[f][-ye:yo])
                
                # multipliziert de zwa sub matrizen mitanonda
                for i in range(len(fa[f][-ye:yo])):
                    res+=workArray[xs:xe][f][ys:ye][i]*fa[f][-ye:yo][i]

                # addiert und speichat in de res array
                resa[x][y] = resa[x][y] + res

    print(resa)

try:
    if __name__ == '__main__':
        applyFilter(workArray, filterArray)

except Exception as e:
    CLIIO.print_to_shell(f'Oh no! Something has gone wrong. {e}\n{traceback.format_exc()}')

finally:
    print('cya')
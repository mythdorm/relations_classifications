import relations

def main():
    result = relations.check_reflexive([[1,0,0],[0,1,0],[0,0,1]])
    print(result)
    result = relations.check_irreflexive([[0,1,0],[0,0,0],[0,1,0]])
    print(result)
    result = relations.make_reflexive([[1,0,0],[0,1,0],[0,0,0]])
    for row in result:
        print(row)
    result = relations.make_reflexive([[1, 0, 0,0], [0, 1, 0,1], [0, 0, 0, 0], [0, 0, 0, 0]])
    for row in result:
        print(row)
    result = relations.check_symmetric([[0,1,0],[0,0,0],[0,0,0]])
    print(result)
    result = relations.check_symmetric([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    print(result)
    for row in [[0, 1, 0], [1, 0, 0], [0, 0, 0]]:
        print(row)
    result = relations.make_symmetric([[0,1,0],[0,0,0],[0,0,0]])
    for row in result:
        print(row)

if __name__ == '__main__':
    main()
#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    for x in range(len(names)):
        if names[x][:2] != "__":
            print(names[x])

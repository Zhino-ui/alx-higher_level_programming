#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    nam = dir(hidden_4)
    for fig in nam:
        if fig[:2] != "__":
            print(fig)

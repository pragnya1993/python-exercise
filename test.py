import sys
import io
import json




def main(element: str):
    with open('test_payload.json','r') as f:
        d = json.load(f)
        d.pop(element,None)
    with open('test_payload.json','w') as f:
        d = json.dump(d,f)


if __name__ == '__main__':
    main(str(sys.argv[1]))

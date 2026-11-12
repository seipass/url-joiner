import argparse,csv,json,sys
def transform(pair):
    from urllib.parse import urljoin
    return urljoin(pair[0],pair[1])

def main():
    parser=argparse.ArgumentParser(description='URL reference joiner')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    data=json.loads(source)
    result=transform(data)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()

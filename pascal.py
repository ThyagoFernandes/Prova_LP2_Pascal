from sys import argv
from contextlib import redirect_stdout

def bin_coeff(n , k): 
	return 1 if k == 0 or k == n else bin_coeff(n-1 , (k-1)) + bin_coeff(n-1 , k) 

if __name__ == "__main__":
    n = int(argv[1])
    ki = int(argv[2])
    k = 0
    linha= [1]
    with open("triangle.out", "w", encoding="utf-8") as out:
        with redirect_stdout(out):
            for i in range(n+1):
                linha.clear()
                linha= [1]
                k = k+1
                for k in range(i):
                    linha.append(linha[k]*(i-k)/(k+1))
                for item in linha:
                    print(item, end=" ")
                print()

from mmc_mdc import MMC_MDC
import os

if __name__ == "__main__":
    os.system('clear')
    n = input("Digite 2 números inteiros: ").split(" ")
    print("MMC",n,'=',MMC_MDC.mmc(n))
    print("MDC",n,'=',MMC_MDC.mdc(n))

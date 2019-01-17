import pandas as pd
import argparse


def writeOutFile(outputDF, outfile):
    outputDF.to_csv(outfile, sep=',', encoding='utf-8', index=False)


def createOutputDF(inputDF, n):
    diff = n - 1
    outputDF = pd.DataFrame()
    for i in range(int(inputDF.shape[0] / n)):
        if i == 0:
            dfl = pd.DataFrame()
            dfl = inputDF.loc[i:(i + n - 1)].T
            new_header = dfl.iloc[0]
            dfl = dfl[1:]
            dfl.columns = new_header
            outputDF = outputDF.append(dfl, ignore_index=False)
        else:
            dfl = pd.DataFrame()
            dfl = inputDF.loc[i + i * diff:(i + i * diff + n - 1)].T
            new_header = dfl.iloc[0]
            dfl = dfl[1:]
            dfl.columns = new_header
            outputDF = outputDF.append(dfl, ignore_index=False)
    return outputDF


def createInitDF(inputfile, d):
    inputDF = pd.read_csv(inputfile, delimiter=d, header=None)
    return inputDF


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Number of rows to be grouped", type=int)
    parser.add_argument(
        "-i", "--inputfile", help="Provide the path of the input file")
    parser.add_argument("-d", "--delimiter", help="Provide the delimiter")
    parser.add_argument(
        "-o", "--outputfile", help="Provide the path of the output file")
    args = parser.parse_args()
    n = args.n
    infile = args.inputfile
    d = args.delimiter
    outfile = args.outputfile
    initDF = createInitDF(infile, d)
    outputDF = createOutputDF(initDF, n)
    writeOutFile(outputDF, outfile)
    print("Please check the putput file generated!")


if __name__ == '__main__':
    main()

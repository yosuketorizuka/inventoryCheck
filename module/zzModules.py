import pandas as pd
import csv
import codecs

class readFileClass():

    df_in = pd.DataFrame()

    def setPara(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename

    def readFile(self):

        # CSVファイルを読み込み
        with codecs.open(self.filepath + self.filename, "r", "Shift-JIS", "ignore") as file:
            df_in = pd.read_csv(file)
        return df_in

class writeFileClass():

    df_out = pd.DataFrame()

    def setPara(self, filepath, filename, df_out):
        self.filepath = filepath
        self.filename = filename
        self.df_out = df_out


    def writeFile(self):
        # CSVファイルを書き出し
        with codecs.open(self.filepath + self.filename, "w", encoding="Shift-JIS") as file:
            self.df_out.to_csv(file, index=False)
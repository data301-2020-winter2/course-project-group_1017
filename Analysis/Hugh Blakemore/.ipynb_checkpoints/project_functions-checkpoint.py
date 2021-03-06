import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("ticks")
sns.set_theme("paper")
def load_and_process(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .assign(Under_BMI= np.where(df1['bmi'] < 18.5 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )
    return df2

def Health(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <=24.9 ) &(df2['smoker'] == 'no') ])
    dfH= dfH.reset_index(drop=True)
    return dfH

def unHealth(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Healthy = np.where( ( (df1['bmi'] <= 24.9)& (df1['smoker'] == 'no') & (df1['bmi'] >= 18.5 ) ),'yes','no'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    
    dfuH = (df2[(df2['bmi'] < 18.5) | (df2['bmi'] >24.9 ) | (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH




def plotAvC(df):
    g=sns.lmplot(x='age', y='charges',data=df, 
          scatter_kws={'s': 100, 'linewidth': 0.5, 'edgecolor': 'w'})
    return g
def brpltEC(df):
    g = sns.countplot(x="Excess_charges",data=df)
    return g
def BrPltECD(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge"
    )
    return g

def BrPltECDh(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge",hue="smoker"
    )
    return g
def BrPltECDB(df):
    g=sns.histplot(
    df, x="Excess_charges", element="bars",
    stat="density",multiple="dodge",hue="bmi"
    )
    return g
def smoker(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] >= 18.5) & (df2['bmi'] <= 24.9 ) & (df2['smoker'] == 'yes') ])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH

def underBmi(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] < 18.5) & (df2['smoker'] == 'no') ])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH

def overBmi(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 24.9 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH
def BoxPlt(df):
    g=sns.boxplot(x='Healthy',y='charges',data=df)
    return g
def BoxPlts(df):
    g=sns.boxplot(x='smoker',y='charges',data=df)
    return g
def BoxPltub(df):
    df1=(df[(df['bmi'] <=24.9 ) &(df['smoker'] == 'no') ])
    g=sns.boxplot(x='Under_BMI',y='charges',data=df1)
    return g
def BoxPltob(df):
    df1=(df[(df['bmi'] >=18.5 ) &(df['smoker'] == 'no') ])
    g=sns.boxplot(x='Over_BMI',y='charges',data=df1)
    return g
def mean(df):
    dfm=df['charges'].mean()
    dfmr = round(dfm,2)
    return dfmr
def allsmoker(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['smoker'] == 'yes')])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH

def obese(url):
    df1 = (
          pd.read_csv(url)
          .rename({'children':'Dependents'},axis=1)
          .dropna(subset=['charges'])
          .drop(['region','Dependents'],axis=1)
          .replace({'southwest':'SW','southeast':'SE','northeast':'NE','northwest':'NW'})
      )
    df2=(df1
         .assign(Excess_charges= np.where(df1['charges'] > 13270 ,'Yes','No'))
         .assign(Over_BMI= np.where(df1['bmi'] > 24.9 ,'Yes','No'))
         .round({"charges":2,"bmi":1})
         .sort_values('charges',ascending=True)
         .reset_index(drop=True)  
    )


    dfuH=(df2[(df2['bmi'] > 40.0 ) & (df2['smoker']=='no')])
    dfuH = dfuH.reset_index(drop=True)
    return dfuH
import pandas as pd

# GÖREV 1

# persona.csv dosyasını okutup ve veri seti ile ilgili genel bilgileri gösterdik.

df = pd.read_csv("datasets/persona.csv")
df.shape
df.info()
df.columns
df.index
df.isnull().values.any()
df.isnull().sum()
df.describe().T

# Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].unique()
df["SOURCE"].value_counts().unique()

# Kaç unique PRICE vardır? Frekansları nedir?
df["PRICE"].nunique()
df["PRICE"].value_counts()

# Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["COUNTRY"].value_counts()

# Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# SOURCE türlerine göre göre satış sayıları nedir?
df["SOURCE"].value_counts()

# Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

# COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# GÖREV 2
# COUNTRY, SOURCE, SEX, AGE kırılımında toplam kazançlar
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# GÖREV 3


agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

# GÖREV 4

agg_df=agg_df.reset_index()

# GÖREV 5
# 'cut' metodu ile age değişkenini belirlediğimiz aralıklara böldük.
agg_df["CAT_AGE"] = pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 70], labels=['0_18', '19_23', '24_30', '31_40',
                                                                               '41_66'])
#Labels aralıkları verilen sayılardan 1 eksik olmalıdır. Zor yoldan öğrendim. Yarım saat uğraştım :)
agg_df.head()

# Görev 6

agg_df["customers_level_based"]=[row[0].upper()+"_"+row[1].upper()+"_"+row[2].upper()+"_"+row[5].upper() for row in agg_df.values]
agg_df.head()

agg_df=agg_df[["customers_level_based","PRICE"]]
# kontrol edelim:
agg_df["customers_level_based"].value_counts()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).reset_index()

# Bu görevde biraz saçmalamış olabilirim ama galiba sonuca ulaştım. :)

# GÖREV 7

# 'qcut' metodu ile müşterileri PRICE ortalamaları düşükten yükseğe 4 segmente ayırdık.
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})
agg_df[agg_df["SEGMENT"] == "C"]

# GÖREV 8

# 2 adet Tahmin

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]



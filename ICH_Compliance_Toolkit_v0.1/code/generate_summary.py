from matplotlib import rcParams
import pandas as pd
import matplotlib.pyplot as plt

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False 

infile = "N100_编码表模板.xlsx"
df = pd.read_excel(infile, sheet_name="data")

yn_cols = [
    "署名（作者/采录者）","表演者（如有）","制作者（录音/录像制作者）",
    "来源/馆藏单位","许可/使用范围说明","采录时间地点（文内是否标注）","敏感性标注（隐私/禁忌）"
]

def miss_rate(series):
    yes = (series=="是").sum()
    no  = (series=="否").sum()
    return (no/(yes+no))*100 if (yes+no)>0 else None

stats = {col: miss_rate(df[col]) for col in yn_cols}
s = pd.Series(stats).sort_values(ascending=False)
s.to_frame("缺漏率(%)").to_excel("summary_table.xlsx")

plt.figure(figsize=(7,4))
s.plot(kind="bar")
plt.ylabel("缺漏率(%)")
plt.title("七要素缺漏率（N样本）")
plt.tight_layout()
plt.savefig("summary_preview.png", dpi=200)
print("已生成 summary_table.xlsx 与 summary_preview.png")

from matplotlib import rcParams
import pandas as pd
import matplotlib.pyplot as plt

rcParams['font.sans-serif'] = ['SimHei']   # 中文字体（本机需安装）
rcParams['axes.unicode_minus'] = False

infile = "templates/N100_编码表模板.xlsx"   # 与仓库目录一致
df = pd.read_excel(infile, sheet_name="data")

yn_cols = [
    "署名（作者/采录者）","表演者（如有）","制作者（录音/录像制作者）",
    "来源/馆藏单位","许可/使用范围说明","采录时间地点（文内是否标注）","敏感性标注（隐私/禁忌）"
]

def miss_rate(series):
    yes = (series == "是").sum()
    no  = (series == "否").sum()
    return (no / (yes + no)) * 100 if (yes + no) > 0 else None

stats = {col: miss_rate(df[col]) for col in yn_cols}
s = pd.Series(stats).sort_values(ascending=False)

# 计算有效样本量（至少在任一要素填过“是/否”的行计入）
valid_rows = df[yn_cols].apply(lambda r: ((r=="是") | (r=="否")).any(), axis=1).sum()

# 输出表格与图
s.to_frame("缺漏率(%)").round(1).to_excel("data/summary_table.xlsx")

plt.figure(figsize=(7,4))
s.plot(kind="bar")
plt.ylabel("缺漏率(%)")
plt.title(f"七要素缺漏率（N={valid_rows}）")
plt.tight_layout()
plt.savefig("data/summary_preview.png", dpi=200)
print("已生成 data/summary_table.xlsx 与 data/summary_preview.png")
存

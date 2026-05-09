import os
import pandas as pd

folder = "data/sample_pdb"
results = []

for file in os.listdir(folder):
    if file.endswith(".pdb"):
        scores = []

        with open(os.path.join(folder,file)) as f:
            for line in f:
                if line.startswith("ATOM"):
                    plddt = float(line[60:66])   # B-factor column
                    scores.append(plddt)

        avg_plddt = sum(scores)/len(scores)

        results.append([file, avg_plddt])

df = pd.DataFrame(results, columns=["Protein_ID","Average_pLDDT"])
df.to_csv("plddt_scores.csv", index=False)

print(df)

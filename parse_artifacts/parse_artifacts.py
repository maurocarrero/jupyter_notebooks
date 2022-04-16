import pandas as pd
import re

def parse_artifact_url(url):
    return re.split('/', url)

def get_df(csv_file):
    return pd.read_csv(csv_file, sep=',')

def main():
    print('Processing artifacts')
    artifacts_csv = '../data/pending_artifacts.csv'
    df = get_df(artifacts_csv)
    artifact_url = df.head(1)
    print(artifact_url)
    result = parse_artifact_url(artifact_url)
    print(result)

main()

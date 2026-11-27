# 安全なAI駆動開発研修

架空の問い合わせCSVを読み込み、カテゴリ別の件数を集計します。
VS CodeのCopilot Chatでコードを作り、GitHubでコミット、レビュー、実行結果の確認を行います。

## 第1回の課題

`summary.py` に、次の仕様を満たす `summarize(path)` 関数を実装してください。

- Python 3.12の標準ライブラリを使う
- UTF-8のCSVを読み、`category` 列の値ごとに件数を辞書で返す
- カテゴリの前後の空白を取り除き、空欄は集計から除外する
- `category` 列があり、ヘッダーしかない場合は空の辞書を返す
- `category` 列がない場合は `ValueError` を送出する
- エラーやログに入力行の全文を出力しない

`data/sample.csv` を集計したときの期待結果は次のとおりです。

```python
{"account": 2, "network": 1}
```

`main` 向けにDraft Pull Requestを開くと、GitHub Actionsでサンプルを実行できます。
実行結果はPRの **Checks** タブに表示されます。

## 第2回の課題

`test_summary.py` を追加し、正常な集計、ヘッダーのみ、空欄・前後の空白、
必須列の不足をテストします。ファイルを追加すると、同じPRでpytestも実行されます。

## 研修で扱う情報

このリポジトリは公開されています。教材、Copilotへの入力、PR本文、
レビューコメントには公開用の架空情報を使ってください。

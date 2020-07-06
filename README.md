# python_vscode_project_template

## 目的

- Pythonプロジェクトに必要な開発環境用の構成のtemplate

## 前提

- python3
  - python3.7以上を使う
    - 特に理由がなければ3.8以上を使う
- poetry
- direnv
  - .envrcにはdotenvと記載
  - .envに開発用の環境変数をまとめる

## ツール

- black
  - 参考: [もうPythonの細かい書き方で議論しない。blackで自動フォーマットしよう](https://blog.hirokiky.org/entry/2019/06/03/202745)
- pytest
  - 参考: [pytest入門 - 闘うITエンジニアの覚え書き](https://www.magata.net/memo/index.php?pytest%C6%FE%CC%E7)
- super-linter
  - Pythonコード以外のlintに使う
- cargo-make
  - ビルドツール。Makefileに抵抗がなければそっちでもOK

## オプション

### RDBへの接続

- PyMySQL
  - MySQL で使用する
- pg8000
  - PostgreSQL or AmazonRedshift で使用する
- SQLAlchemy
  - 大規模プロジェクトでのみ使用する
- Pandas
  - 複数RDBMSへの接続やファイルとDBのデータのJOIN等が必要な場合に使用する
- Jupyter
  - REPL的に検証したい場合や、検証内容を保存しておきたいときに使用する

### 開発

- 依存パッケージのインストール: `poetry install`
- test実行: `makers --env-file .env tests`
- superlint実行: `makers --env-file .env lints`

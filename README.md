# PDF をブックレット化する

```
bookletnize input.pdf output.pdf
```

生成された PDF を 2 枚レイアウト、短辺綴じで印刷するとブックレットになるはず。

## install

```
pip install git+https://github.com/74th/pdf-bookletnize

pipx install git+https://github.com/74th/pdf-bookletnize


bookletnize -h
```

## develop

```
poetry install
portry run bookletnize input.pdf output.pdf
```

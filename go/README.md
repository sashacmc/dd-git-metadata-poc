Build
```bash
go build -o gitmetadatapoc
```

Alternative build
```bash
go build -ldflags="-X 'ddtrace.repository_url=`git config --get remote.origin.url`'" -o ./gitmetadatapoc
```

Run
```bash
./gitmetadatapoc
```

Extract metadata
```bash
go version -m ./gitmetadatapoc
```

Init new app
```bash
npx degit "rollup/rollup-starter-app" gitmetadatapoc
```

Compile
```bash
rollup -c --environment DD_GIT_COMMIT_SHA:$(git rev-parse HEAD) --environment DD_GIT_REPOSITORY_URL:$(git config --get remote.origin.url)  --bundleConfigAsCjs
```

Run
```bash
node test.cjs
```

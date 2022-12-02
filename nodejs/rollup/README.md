Init new app
```bash
npx degit "rollup/rollup-starter-app" gitmetadatapoc
npm install --save-dev rollup-plugin-inject-process-env
```

Compile
```bash
rollup -c --bundleConfigAsCjs
```

Run
```bash
node test.cjs
```

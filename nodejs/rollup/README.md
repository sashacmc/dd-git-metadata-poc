npx degit "rollup/rollup-starter-app" gitmetadatapoc

rollup src/main.js -o bundle.js -f cjs

node test.js

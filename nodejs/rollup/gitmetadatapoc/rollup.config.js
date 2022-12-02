// rollup.config.js
const injectProcessEnv = require('rollup-plugin-inject-process-env')
export default {
  input: 'src/main.cjs',
  output: {
    file: 'bundle.cjs',
    format: 'cjs'
  },
  plugins: [
	injectProcessEnv({ 
      DD_GIT_COMMIT_SHA: process.env.DD_GIT_COMMIT_SHA,
      DD_GIT_REPOSITORY_URL: process.env.DD_GIT_REPOSITORY_URL,
	}),
  ],
};

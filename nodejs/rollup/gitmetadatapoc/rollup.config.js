// rollup.config.js
const injectProcessEnv = require('rollup-plugin-inject-process-env')
const child_process = require('child_process');

function git(command) {
  return child_process.execSync(`git ${command}`, { encoding: 'utf8' }).trim();
}

export default {
  input: 'src/main.cjs',
  output: {
    file: 'bundle.cjs',
    format: 'cjs'
  },
  plugins: [
    injectProcessEnv({ 
      DD_GIT_REPOSITORY_URL: git('config --get remote.origin.url'),
      DD_GIT_COMMIT_SHA: git('rev-parse HEAD'),
    }),
  ],
};

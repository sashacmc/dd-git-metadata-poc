const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const child_process = require('child_process');
function git(command) {
	return child_process.execSync(`git ${command}`, { encoding: 'utf8' }).trim();
}

module.exports = {
	entry: './src/main.js',
	mode: 'production',
	output: {
		path: path.resolve(__dirname, 'dist'),
		filename: 'gitmetadatapoc-webpack.bundle.js',
	},
	plugins: [
		new webpack.EnvironmentPlugin({
			DD_GIT_REPOSITORY_URL: git('config --get remote.origin.url'),
			DD_GIT_COMMIT_SHA: git('rev-parse HEAD'),
		}),
	]
};

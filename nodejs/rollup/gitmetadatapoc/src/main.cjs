// src/main.js
const tracer = require('dd-trace').init()
import foo from './foo.js';

export default function () {
	tracer.trace('some trace', { resource: 'some_resource' }, () => {
		const span = tracer.scope().active()
		span.setTag('git.commit.sha', process.env.DD_GIT_COMMIT_SHA)
		span.setTag('git.repository_url', process.env.DD_GIT_REPOSITORY_URL)

		try {
			console.log(foo)
			throw new Error('some error')
		} catch (e) {
			span.setTag('error', e)
		}
	})
}

console.log('git.commit.sha', process.env.DD_GIT_COMMIT_SHA)
console.log('git.repository_url', process.env.DD_GIT_REPOSITORY_URL)

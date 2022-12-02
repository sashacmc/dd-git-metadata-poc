// src/main.js
const tracer = require('dd-trace').init()
import foo from './foo.js';

export default function () {
  tracer.trace('some trace', { resource: 'some_resource' }, () => {
    const span = tracer.scope().active()
	console.log(foo);
    try {
	  throw new Error('some error')
	} catch (e) {
	  span.setTag('error', e)
	}
  })
}

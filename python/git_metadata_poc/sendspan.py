import ddtrace

span = ddtrace.tracer.trace("gitmetadata.test.span")

span.finish()

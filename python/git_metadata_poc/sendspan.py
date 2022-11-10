import ddtrace

with ddtrace.tracer.trace("gitmetadata.test.span"):
    raise Exception("some error")
